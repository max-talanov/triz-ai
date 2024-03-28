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


Thank you for using TRIZ-AI!
