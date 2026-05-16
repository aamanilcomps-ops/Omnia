python
from omnia.agents.nlp_agent import NLPAgent
class App:
    def __init__(self):
        self.nlp_agent = NLPAgent()
    def run(self):
        input = "This is a test input."
        output = self.nlp_agent.process(input)
        print(output)
if __name__ == "__main__":
    app = App()
    app.run()
