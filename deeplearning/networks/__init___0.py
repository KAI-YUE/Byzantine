# My Libraries
from deeplearning.networks.lenet import LeNet, LeNet_5
from deeplearning.networks.resnet import ResNet18
from deeplearning.networks.resnet_nonorm import ResNet18_
from deeplearning.networks.vgg import VGG_7

nn_registry = {
    "lenet":            LeNet,
    "lenet_5":          LeNet_5,

    "resnet18":         ResNet18,

    "resnet18_":        ResNet18_,

    "vgg_7":            VGG_7,
}
