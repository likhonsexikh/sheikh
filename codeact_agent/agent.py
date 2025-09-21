import json

class Agent:
    def __init__(self, model_path="model/sheikh.gguf"):
        """
        Initializes the CodeAct Agent.
        In a real implementation, this would load the Sheikh model.
        """
        print(f"Initializing agent with model: {model_path}")
        # Placeholder for model loading logic
        self.model = None
        self.tools = {}

    def register_tool(self, tool_function):
        """
        Registers a tool for the agent to use.
        """
        self.tools[tool_function.__name__] = tool_function
        print(f"Registered tool: {tool_function.__name__}")

    def run(self, prompt):
        """
        Runs the agent with a given prompt.
        This is a placeholder and does not actually use a real LLM.
        """
        print(f"\nReceived prompt: {prompt}")

        # 1. Use the LLM to decide which tool to use.
        #    (Simulating this part for now)
        print("Thinking... (simulating LLM decision making)")

        # For this placeholder, we'll hardcode the tool choice based on keywords.
        if "create a file" in prompt:
            tool_name = "create_file"
            # In a real scenario, the model would generate this JSON
            tool_params_json = '{"filename": "test.txt", "content": "Hello from CodeAct Agent!"}'
            tool_params = json.loads(tool_params_json)
        else:
            print("No suitable tool found for this prompt.")
            return

        print(f"Decided to use tool: {tool_name} with params: {tool_params}")

        # 2. Execute the chosen tool.
        if tool_name in self.tools:
            tool_function = self.tools[tool_name]
            try:
                result = tool_function(**tool_params)
                print(f"Tool executed successfully. Result: {result}")
                return result
            except Exception as e:
                print(f"Error executing tool {tool_name}: {e}")
                return f"Error: {e}"
        else:
            print(f"Tool '{tool_name}' not found.")
            return f"Error: Tool '{tool_name}' not found."
