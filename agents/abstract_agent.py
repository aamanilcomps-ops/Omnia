python
from abc import ABC, abstractmethod
class AbstractAgent(ABC):
    @abstractmethod
    def process(self, input):
        pass
