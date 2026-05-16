python
from abc import ABC, abstractmethod
import torch
import torch.nn as nn
class BaseModel(ABC):
    @abstractmethod
    def train(self, data):
        pass
    @abstractmethod
    def predict(self, input):
        pass
class NeuralNetworkModel(BaseModel):
    def __init__(self):
        self.model = nn.Sequential(
            nn.Linear(784, 128),
            nn.ReLU(),
            nn.Linear(128, 10),
            nn.Softmax()
        )
    def train(self, data):
        # add training logic here
        pass
    def predict(self, input):
        return self.model(input)
