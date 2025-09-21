# examples/codeact_agent_example.py

import sys
import os

# Add the project root to the Python path to allow importing from other directories
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from codeact_agent.agent import Agent
from codeact_agent.tools.file_tools import create_file

def main():
    """
    Main function to demonstrate the CodeAct Agent.
    """
    print("--- Running CodeAct Agent Example ---")

    # 1. Initialize the agent
    agent = Agent()

    # 2. Register the self-contained tool with the agent
    agent.register_tool(create_file)

    # 3. Create a prompt for the agent
    prompt = "Please create a file named 'agent_test.txt' and write 'Hello from the agent!' into it."

    # 4. Run the agent with the prompt
    # In this placeholder, the agent will use the hardcoded logic to call the tool.
    agent.run(prompt)

    # 5. Verify that the file was created
    if os.path.exists("agent_test.txt"):
        print("\nVerification: 'agent_test.txt' was created successfully.")
        with open("agent_test.txt", 'r') as f:
            print(f"File content: '{f.read()}'")
        # Clean up the created file
        os.remove("agent_test.txt")
        print("Cleaned up 'agent_test.txt'.")
    else:
        print("\nVerification failed: 'agent_test.txt' was not created.")

    print("\n--- Example Finished ---")

if __name__ == "__main__":
    main()
