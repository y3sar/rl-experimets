import torch.nn as nn
from collections import OrderedDict
import torch




class PolicyNet(nn.Module):
    def __init__(self, action_space, feature_shape):
        super().__init__()
        self.action_space = action_space
        self.state_shape = feature_shape

        self.conv_layer = OrderedDict([
                            ('conv1', nn.Conv2d(3, 8, kernel_size=5)),
                            ('relu1', nn.ReLU()),
                            ('conv2', nn.Conv2d(8, 20, kernel_size=5)),
                            ('relu2', nn.ReLU()),
                            ('conv3', nn.Conv2d(20, 30, kernel_size=5)),
                            ('relu3', nn.ReLU()),
                           
                           ])
        
        self.arch = OrderedDict([
                    ('fc1', nn.Linear(139200, 250)),
                    ('relu1', nn.ReLU()),

                    ('fc2', nn.Linear(250, 150)),
                    ('relu2', nn.ReLU()),
                    ('fc3', nn.Linear(150, 50)),
                    ('relu3', nn.ReLU()),
                    ('fc4', nn.Linear(50, self.action_space))
                    ])

        self.model = nn.Sequential(self.arch)
        self.conv_model = nn.Sequential(self.conv_layer)

    def forward(self, x):
        x = self.conv_model(x)
        x = x.view(x.shape[0], -1)
        
        x = self.model(x)
        return torch.log_softmax(x, dim=1)


