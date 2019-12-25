print('importing libs...')

import torch
import torchvision
import requests

print('loading model...')
res34 = torchvision.models.resnet34(pretrained=True, progress=True)

print('loading iamge...')
input_images = torchvision.datasets.ImageFolder(
        root='./test_images/',
        transform=torchvision.transforms.ToTensor()
    )


model_input = input_images[0][0].reshape(1,3,1600,1200)

#print(input_images[0][0].reshape(1,3,1600,1200).size())


url = 'https://gist.githubusercontent.com/yrevar/942d3a0ac09ec9e5eb3a/' \
      'raw/596b27d23537e5a1b5751d2b0481ef172f58b539/imagenet1000_clsid_to_human.txt'

print('reading classes...')
imagenet_classes = eval(requests.get(url).content)

print('model inference...')
raw_result = res34(model_input)

probs = torch.nn.functional.softmax(raw_result[0], dim=0)
res_index = probs.argmax()
print('index: ', res_index)
print(res_preds)
print('res50 predicted ', imagenet_classes[res_index], ' confidence: ', probs[res_index], '\n')