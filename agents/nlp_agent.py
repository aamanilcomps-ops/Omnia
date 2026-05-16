python
from transformers import pipeline
from .abstract_agent import AbstractAgent
class NLPAgent(AbstractAgent):
    def __init__(self):
        self.summarizer = pipeline("summarization")
    def process(self, input):
        return self.summarizer(input, max_length=50, clean_up_tokenization_spaces=True)
