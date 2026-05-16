python
from PIL import Image
from torchvision import models, transforms
from .abstract_agent import AbstractAgent
class CVAgent(AbstractAgent):
    def __init__(self):
        self.model = models.densenet121(pretrained=True)
        self.transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
    def process(self, input):
        img = Image.open(input)
        img_t = self.transform(img)
        batch_t = torch.unsqueeze(img_t, 0)
        out = self.model(batch_t)
        return out
