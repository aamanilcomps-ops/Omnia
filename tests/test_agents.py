python
import unittest
from omnia.agents.nlp_agent import NLPAgent
class TestNLPAgent(unittest.TestCase):
    def test_process(self):
        agent = NLPAgent()
        input = "This is a test input."
        output = agent.process(input)
        self.assertIsNotNone(output)
