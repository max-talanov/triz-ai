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
    with st.expander("Show Main TRIZ ARIZ Definitions"):
        st.write("""
        **ARIZ (Algorithm of Inventive Problem Solving):**
        ARIZ is a systematic and structured methodology for complex problem solving, primarily used within the TRIZ framework for innovation and invention. It provides a step-by-step approach to navigate from problem identification to the implementation of novel solutions by overcoming psychological inertia, and utilizing inventive principles and patterns.
        
        **Key Components of ARIZ Include:**
        - **Problem Definition:** Detailed analysis of the problem to fully understand its nature and context.
        - **Problem Modeling:** Transforming the real-life problem into a generalized model that discloses contradictions.
        - **Solution Generation:** Using TRIZ tools such as the contradiction matrix, 40 inventive principles, and separation principles to generate solutions.
        - **Solution Analysis and Selection:** Evaluating generated solutions based on their novelty, technical feasibility, and potential for impact.
        - **Implementation Planning:** Detailed planning on how the solution can be implemented in the real world scenario.

        ARIZ is often considered as a more advanced tool within the TRIZ toolkit, intended for tackling more complex and less straightforward problems where simpler TRIZ tools might not suffice.
        """)
        
        st.write("""
        **TRIZ:** Developed by Genrich Altshuller and his colleagues starting in 1946, TRIZ is a problem-solving, analysis, and forecasting tool derived from the study of patterns of invention in the global patent literature. It provides a systematic approach for understanding and solving inventive problems and developing new innovations. TRIZ presents a practical methodology for ideation that enables the creation of innovative solutions based on previously solved problems.
        """)

    
        st.write("""
        **State of the Art (SOTA):** Refers to the highest level of development, as of a device, technique, or scientific field, achieved at a particular time. It often represents the most advanced stage of technical development or the best performance achieved in a particular technology or industry.
        """)

    
        st.write("""
        **Ideal Final Result (IFR):** A key concept in TRIZ, the Ideal Final Result is the best possible solution for a problem scenario, where the desired outcome is achieved without any negative consequences. The IFR is theoretically the best version of a system or product, involving minimal cost and complexity while maximizing benefits.
        """)

    
        st.write("""
        **Technical Contradiction:** In TRIZ, a technical contradiction occurs when an improvement in one parameter of a system leads to the degradation of another parameter. Identifying and resolving these contradictions is critical for effective problem-solving in TRIZ. This concept encourages looking for solutions that resolve conflicts between opposing forces or requirements.
        """)
    local_image_path = 'im-TRIZ_AI.png'
    st.image([local_image_path], caption=['This figure illustrates the structured approach using an intelligent agent to streamline the innovation process, from problem identification through solution development and testing.'])
    st.markdown("**Step 1 out of 7.**", unsafe_allow_html=True)

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
                st.markdown("**Step 2 out of 7.**  Generating IFR...", unsafe_allow_html=True)
                st.session_state["ifr"] = query_gpt(
                    f"Describe the ideal final result (IFR) for the following problem: {problem_description} with the following limitations: Budget limitation is {budget_limitation}, Other limitations: {other_limitations}"
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
            st.markdown("**Step 3 out of 7.**  Checking if SOTA (State of the art) exists for such an IFR...", unsafe_allow_html=True)
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
                f"The solution for this problem does not exist on the market. {st.session_state['sota_exists']['explanation']}"
            )
            st.info("Generating technical contradictions...")
            # If no SOTA exists, proceed to generate technical contradictions
            st.session_state["technical_contradictions"] = query_gpt_json(
                f"Describe 4 technical contradictions of the IFR? IFR: {st.session_state['ifr']} Generate a list of 4 TCs in JSON format: 'list': [TC1, TC2]"
            )["list"]
            # Displaying technical contradictions before selection
            st.markdown("**Step 4 out of 7.**  Technical contradictions highlight the key areas where improvements are needed to develop innovative solutions. Please, select technical contradictions:", unsafe_allow_html=True)
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
            st.markdown("**Step 5 out of 7.**  Updating IFR based on the selected contradictions...", unsafe_allow_html=True)
            st.session_state["ifr"] = query_gpt(
                f"Update the following IFR {ifr} taking these TCs into account: {st.session_state['selected_contradictions']}"
            )
            st.write(st.session_state["ifr"])

    # Step 5: Solve Technical Contradictions
    if "contradictions_selected" in st.session_state:
        st.markdown("**Step 6 out of 7.**  Solving selected contradictions...", unsafe_allow_html=True)
        st.session_state["solved_contradictions"] = query_gpt(
            f"Taking this IFR into account: {st.session_state['ifr']}, solve the following contradictions: {st.session_state['selected_contradictions']} "
        )
        st.info(st.session_state["solved_contradictions"])
        # Implement logic to solve contradictions and display solutions
        # This might involve additional interactions with GPT based on selected contradictions
        st.session_state["compare_with_sota"] = query_gpt(
            f"Compare these techinical contradictions with the current state of the art: {st.session_state['solved_contradictions']}"
        )
        st.markdown("**Step 7 out of 7.**  Comparing these technical contradictions with SOTA...", unsafe_allow_html=True)
        st.info(st.session_state["compare_with_sota"])

        st.info("Congratulations! You have successfully generated your problem statement using our application. If you wish to start a new session or generate another problem statement, please restart the page.")

if __name__ == "__main__":
    main()
