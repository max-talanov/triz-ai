import streamlit as st
from openai import OpenAI
import json

client = OpenAI()


def query_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        temperature=1,
        max_tokens=1600,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        messages=[
            {
                "role": "system",
                "content": """You are a helpful assistant, well-versed in TRIZ and ARIZ principles.""",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )
    return response.choices[0].message.content


def query_gpt_json(prompt):
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        temperature=1,
        max_tokens=1600,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        messages=[
            {
                "role": "system",
                "content": """You are a helpful assistant, well-versed in TRIZ and ARIZ principles.""",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        response_format={"type": "json_object"},
    )
    return json.loads(response.choices[0].message.content)


def main():
    st.title("TRIZ Flow Application")
    st.info("Step 1 out of 6.")

    # Step 1: Initial Input
    if "initial_input_done" not in st.session_state:
        with st.form("initial_input"):
            problem_description = st.text_area(
                "Describe the problem you are trying to solve."
            )
            other_limitations = st.text_area("Describe other limitations (if any).")
            budget_limitation = st.text_area("Is there a budget limitation?")
            submitted = st.form_submit_button("Submit")

            if submitted:
                st.session_state["initial_input_done"] = True
                st.session_state["problem_description"] = problem_description
                st.session_state["other_limitations"] = other_limitations
                st.session_state["budget_limitation"] = budget_limitation
                # Generate IFR Here
                st.info("Step 2 out of 6. Generating IFR...")
                st.session_state["ifr"] = query_gpt(
                    f"Describe the ideal final result (IFR) for the following. Problem: {problem_description}\nLimitations: {other_limitations}\nBudget: {budget_limitation}"
                )

    # Step 2: Validate IFR
    if (
        "initial_input_done" in st.session_state
        and "ifr_validated" not in st.session_state
    ):
        st.write(st.session_state["ifr"])
        if st.button("IFR is fine"):
            st.session_state["ifr_validated"] = True
            # Check if SOTA exists for such an IFR
            st.info("Step 3 out of 6. Checking if SOTA (State of the art) exists for such an IFR...")
            st.session_state["sota_exists"] = query_gpt_json(
                f"Check if a state of the art solution exists for such an IFR. IFR: {st.session_state['ifr']}. Generate the following json: 'exists': 'True' or 'False', 'explanation': explain why it exists"
            )
        elif st.button("Regenerate IFR"):
            # Regenerate IFR Here
            ifr = st.session_state["ifr"]
            st.session_state["ifr"] = query_gpt(
                f"Describe the ideal final result (IFR) for the following. Problem: {st.session_state['problem_description']}\nLimitations: {st.session_state['other_limitations']}\nBudget: {st.session_state['budget_limitation']}. This IFR was not good enough: {ifr}, generate another one."
            )

    # Step 3: SOTA Check
    if "ifr_validated" in st.session_state and st.session_state["sota_exists"]:
        if st.session_state["sota_exists"]["exists"].lower() == "true":
            st.error(
                f"The solution for this problem is already available on the market. Please, restart the chat to start over. Explanation: {st.session_state['sota_exists']['explanation']}"
            )
            return  # End the flow
        else:
            st.info(
                f"The solution for this problem does not exist on the market, continuing... Explanation: {st.session_state['sota_exists']['explanation']}"
            )
            st.info("Generating technical contradictions...")
            # If no SOTA exists, proceed to generate technical contradictions
            st.session_state["technical_contradictions"] = query_gpt_json(
                f"Describe 4 technical contradictions of the IFR? IFR: {st.session_state['ifr']} Generate a list of 4 TCs in JSON format: 'list': [TC1, TC2]"
            )["list"]
            # Displaying technical contradictions before selection
            st.info("Step 4 out of 6. Technical contradictions highlight the key areas where improvements are needed to develop innovative solutions. Please, select technical contradictions:")
            for tc in st.session_state["technical_contradictions"]:
                st.info(tc)

    # Step 4: Select Technical Contradictions
    if (
        "technical_contradictions" in st.session_state
        and "contradictions_selected" not in st.session_state
    ):
        selected = st.multiselect(
            "Select one or more contradictions:",
            st.session_state["technical_contradictions"],
            [],
        )
        if st.button("Submit Contradictions"):
            st.session_state["selected_contradictions"] = selected
            st.session_state["contradictions_selected"] = True

            ifr = st.session_state["ifr"]
            st.info("Updating IFR based on the selected contradictions...")
            st.session_state["ifr"] = query_gpt(
                f"Update the following IFR {ifr} taking these TCs into account: {st.session_state['selected_contradictions']}"
            )
            st.write(st.session_state["ifr"])

    # Step 5: Solve Technical Contradictions
    if "contradictions_selected" in st.session_state:
        st.info("Step 5 out of 6. Solving selected contradictions...")
        st.session_state["solved_contradictions"] = query_gpt(
            f"Taking this IFR into account: {st.session_state['ifr']}, solve the following contradictions: {st.session_state['selected_contradictions']} "
        )
        st.info(st.session_state["solved_contradictions"])
        # Implement logic to solve contradictions and display solutions
        # This might involve additional interactions with GPT based on selected contradictions
        st.session_state["compare_with_sota"] = query_gpt(
            f"Compare these techinical contradictions with the current state of the art: {st.session_state['solved_contradictions']}"
        )
        st.info("Step 6 out of 6. Comparing these technical contradictions with SOTA...")
        st.info(st.session_state["compare_with_sota"])

        st.info("Congratulations! You have successfully generated your problem statement using our application. If you wish to start a new session or generate another problem statement, please restart the page.")

if __name__ == "__main__":
    main()
