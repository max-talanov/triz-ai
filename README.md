# triz-ai
TRIZ-AI project repository. The implementation of the TRIZ methodology over intellectual agents.

Thank you for your interest in the TRIZ-AI project. This README will guide you through the process of setting up and running the codebase, which utilizes the OpenAI API for various AI-related tasks.

## Getting Started

### Step 1: Cloning the Repository

1. Clone the repository from GitHub using the following command:
git clone https://github.com/max-talanov/triz-ai.git

Ensure that you navigate to the `backend` branch of the repository for the latest updates related to the backend functionality.

2. Once the repository is cloned, navigate to the downloaded directory.

### Step 2: Setting up Python

To run the codebase, you need to have Python installed on your system. Follow these steps to ensure you have Python set up:

#### Install Python:
- If you already have Python installed, ensure it's at least version 3.7.1 or newer.
- If Python is not installed or you need to update it, download and install the latest version from the [official Python website](https://www.python.org/).

### Step 3: Install the OpenAI Python Library

The TRIZ-AI codebase utilizes the OpenAI Python library. Follow these steps to install it:

1. Open your terminal or command prompt.
2. Run the following command:
pip install --upgrade openai


### Step 4: Set Up Your API Key

To interact with the OpenAI API, you need an API key. Follow these instructions to set up your API key:

#### For MacOS:
1. Open Terminal.
2. Edit Bash Profile using the command:
nano ~/.bash_profile

or for newer MacOS versions:
nano ~/.zshrc
3. Add the following line to the file, replacing `your-api-key-here` with your actual API key:
export OPENAI_API_KEY='your-api-key-here'
4. Save and exit the editor by pressing `Ctrl+O` to write changes, followed by `Ctrl+X` to close the editor.
5. Load your profile by using the command:
source ~/.bash_profile 
or
source ~/.zshrc
6. Verify the setup by typing:
echo $OPENAI_API_KEY

#### For Windows:
1. Open Command Prompt.
2. Set the environment variable in the current session using the command:
setx OPENAI_API_KEY "your-api-key-here"
This sets the `OPENAI_API_KEY` environment variable for the current session.
3. To make the setup permanent:
- Right-click on 'This PC' or 'My Computer' and select 'Properties'.
- Click on 'Advanced system settings'.
- Click the 'Environment Variables' button.
- In the 'System variables' section, click 'New...' and enter `OPENAI_API_KEY` as the variable name and your API key as the variable value.
4. Verify the setup by reopening the command prompt and typing:
echo %OPENAI_API_KEY%

### Step 5: Running the Code

Once Python is installed, the OpenAI library is set up, and your API key is configured, you can run the TRIZ-AI code. Navigate to the directory where you cloned the repository and execute the necessary Python scripts or commands as per the project's documentation or instructions.

## Key Terminologies

Understanding the following key terms will enhance your experience with the application:

- **TRIZ:** An acronym for "Teoriya Resheniya Izobretatelskikh Zadach" (Theory of Inventive Problem Solving), TRIZ is a methodology based on patent literature analysis for solving invention-related problems and forecasting technology development.

- **SOTA (State of the Art):** Represents the highest level of development achieved at a given time, as of a device, technique, or scientific field. Knowing if a SOTA solution exists for your problem is crucial for assessing the novelty of your approach.

- **IFR (Ideal Final Result):** A concept in TRIZ representing the best possible solution to a problem, achieving the desired outcome with minimal resources and no negative impacts.

## How to Use the Application

Follow these steps to navigate through the problem-solving process:

1. **Initial Input:** Describe the problem in detail, along with any limitations that might affect the solution. This information lays the foundation for generating an effective solution.

2. **Generating the Ideal Final Result (IFR):** The application will generate an IFR based on your input. Review it and ensure it meets your expectations before proceeding.

3. **State of the Art (SOTA) Check:** The application assesses whether a SOTA solution exists for your problem. If one does, consider refining your problem statement or exploring improvements to existing solutions.

4. **Identifying Technical Contradictions:** You'll identify technical contradictions that prevent achieving the IFR. Select the most relevant contradictions to address.

5. **Solving Technical Contradictions:** The application offers solutions to the selected contradictions, moving you closer to realizing the IFR.

6. **Comparison with SOTA:** Finally, compare the solved contradictions with the current SOTA to evaluate the novelty and feasibility of your solution.

### Tips for Users

- **Patience is Key:** Generating responses for complex analyses can take time. Please wait for the application to process your inputs.

- **Be Specific:** Detailed descriptions of your problem, limitations, and expectations lead to more accurate and applicable solutions.

- **Iterative Process:** Problem-solving is often non-linear. Feel free to revisit earlier steps based on new insights or if outcomes don't align with your goals.

This guide aims to facilitate your journey through the TRIZ Flow Application. Remember, innovation is a process, and this tool is here to guide you every step of the way. Happy problem-solving!

Thank you for using TRIZ-AI!
