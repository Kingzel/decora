from PIL import Image
from transformers import pipeline

vqa_pipeline = pipeline("visual-question-answering", model="dandelin/vilt-b32-finetuned-vqa")

image =  Image.open("C:/Users/iffat/Downloads/pillow.jpg")
question = "describe object"

por = vqa_pipeline(image, question, top_k=10)
print(por)