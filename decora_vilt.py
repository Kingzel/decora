from PIL import Image
from transformers import pipeline
import os


# question = "vibe of this object"
# question2 = 'is this danger'
# question3 = 'color


def query(url: str, question: str, k : int):
    vqa_pipeline = pipeline("visual-question-answering", model="dandelin/vilt-b32-finetuned-vqa")
    image =  Image.open("C:/Users/ishan/Downloads/ezgif-1-5d3305ee3c.jpg")
    por = vqa_pipeline(image, question, top_k=k)
    os.system("cls")
    return por