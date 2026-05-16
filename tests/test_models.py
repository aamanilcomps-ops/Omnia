python
import unittest
from omnia.models.model import NeuralNetworkModel
class TestNeuralNetworkModel(unittest.TestCase):
    def test_train(self):
        model = NeuralNetworkModel()
        data = torch.randn(1, 784)
        model.train(data)
        self.assertIsNotNone(model.model.state_dict())
