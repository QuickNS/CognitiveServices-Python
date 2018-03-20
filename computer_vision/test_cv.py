from computer_vision import ComputerVisionService
from PIL import Image
from io import BytesIO
import json

import matplotlib.pyplot as plt
cv = ComputerVisionService('westeurope', 'ff540c4558cf45999a2fc6c33bcee98c')

person = 'http://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/images/woman_roof_face.png'
two_persons = 'https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/images/mom_daughter_face.png'

#tags
#result = cv.analyzeUrl('https://docs.microsoft.com/en-us/azure/cognitive-services/Computer-vision/images/house_yard.jpg', 'Tags')
#print(json.dumps(result, indent=4))

#categories
#result = cv.analyzeUrl('https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/images/cute_dog.jpg', 'Categories')
#print(json.dumps(result, indent=4))

#result = cv.analyzeUrl('https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/images/mountain_vista.jpg', 'Categories')
#print(json.dumps(result, indent=4))

#result = cv.analyzeUrl('https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/images/woman_roof.jpg', 'Categories')
#print(json.dumps(result, indent=4))

#Image Type
#result = cv.analyzeUrl('https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/images/cheese_clipart.jpg', 'ImageType')
#print(json.dumps(result, indent=4))

#result = cv.analyzeUrl('https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/images/lion_drawing.jpg', 'ImageType')
#print(json.dumps(result, indent=4))

#result = cv.analyzeUrl('https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/images/flower.jpg', 'ImageType')
#print(json.dumps(result, indent=4))

#result = cv.listDomainModels()
#print(json.dumps(result, indent=4))

image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Cursive_Writing_on_Notebook_paper.jpg/800px-Cursive_Writing_on_Notebook_paper.jpg"
result = cv.recognizeTextWithUrl(image_url)
print(result)

import time
import requests

analysis = {}
while not "recognitionResult" in analysis:
    analysis = cv.checkRecognizeTextStatus(result)

polygons = [(line["boundingBox"], line["text"]) for line in analysis["recognitionResult"]["lines"]]
print(polygons)