import unittest
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from codeact_agent.agent import Agent
from codeact_agent.tools.file_tools import create_file

class TestCodeActAgent(unittest.TestCase):

    def setUp(self):
        """Set up a new agent before each test."""
        self.agent = Agent()

    def test_agent_initialization(self):
        """Test that the agent initializes correctly."""
        self.assertIsNotNone(self.agent)
        self.assertEqual(self.agent.tools, {})

    def test_register_tool(self):
        """Test that a tool can be registered."""
        self.agent.register_tool(create_file)
        self.assertIn("create_file", self.agent.tools)
        self.assertEqual(self.agent.tools["create_file"], create_file)

    def test_run_agent_with_tool(self):
        """
        Test running the agent with a prompt that should trigger a tool.
        This test uses the placeholder logic in the agent.
        """
        self.agent.register_tool(create_file)
        prompt = "create a file"
        result = self.agent.run(prompt)

        # The placeholder agent creates 'test.txt'. We need to check for it and clean up.
        self.assertTrue(os.path.exists("test.txt"))
        with open("test.txt", 'r') as f:
            self.assertEqual(f.read(), "Hello from CodeAct Agent!")

        os.remove("test.txt") # cleanup
        self.assertIn("File 'test.txt' created successfully.", result)

if __name__ == '__main__':
    unittest.main()
