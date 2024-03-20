from openai import OpenAI

client = OpenAI()

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", "content": "You are a helpful assistant, well-versed in TRIZ and ARIZ principles."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def user_input(prompt):
    return input(prompt)

def decision_point(question, options):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    choice = int(user_input("Select an option: "))
    return options[choice-1]

def generate_ifr(problem_description, budget_limitation, other_limitations, num_ifrs=1):
    prompt = f"Could you please describe the ideal final result (IFR) for the following problem: {problem_description} with the following limitations: Budget limitation is {'none' if not budget_limitation else budget_limitation}, Other limitations: {other_limitations}?"
    return chat_with_gpt(prompt)

# The user inputs their problem and limitations
problem_description = user_input("Describe the problem you are trying to solve: ")
budget_limitation = user_input("Is there a budget limitation? No / Yes, specify the amount: ")
other_limitations = user_input("Describe other limitations (if any): ")
num_ifrs = 1

# Initialize loop control variables
satisfied_with_ifr = False
ifr = ""

    
while not satisfied_with_ifr:
    ifr = generate_ifr(problem_description, budget_limitation, other_limitations, num_ifrs)
    print("Generated IFR:", ifr)
    # Ask if the user is satisfied with the IFR
    decision = decision_point("Are you satisfied with this IFR or would you like to generate another one?", ["I am satisfied with this IFR.", "Generate another IFR."])
    satisfied_with_ifr = decision == "I am satisfied with this IFR."

def compare_ifr_to_sota(ifr):
    prompt = f"Could you please compare the above IFR with the SOTA, and find out if the solution already exists and is available on the market? IFR: {ifr}"
    return chat_with_gpt(prompt)

def step_back_from_ifr(ifr):
    prompt = f"Could you please take one step back from the IFR, and describe the updated IFR? Current IFR: {ifr}"
    return chat_with_gpt(prompt)

def describe_technical_contradictions(ifr):
    prompt = f"Could you please describe 4 technical contradictions of the ideal final result ({ifr}) and name them 'TC1', 'TC2', 'TC3', 'TC4'?"
    return chat_with_gpt(prompt)

def solve_technical_contradictions(tc_names):
    prompt = f"Could you please use TRIZ standards to solve the technical contradictions ({', '.join(tc_names)}) described earlier?"
    return chat_with_gpt(prompt)

def compare_solution_to_sota(solution):
    prompt = f"Could you please compare the solution that you provided with the state-of-the-art? Solution: {solution}"
    return chat_with_gpt(prompt)

# Step 2: SOTA comparison
sota_comparison = compare_ifr_to_sota(ifr)
print("SOTA Comparison:", sota_comparison)

