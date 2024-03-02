from PIL import Image
from transformers import pipeline
import os
from enum import Enum



questions=[   "describe vibe",
    "color", "type of design furniture", 'identify furniture']
    
# b

# question = "vibe of this object"
# question2 = 'is this danger'
# question3 = 'color
enumerate

def query(url: str, question: str, k : int):
    vqa_pipeline = pipeline("visual-question-answering", model="dandelin/vilt-b32-finetuned-vqa")
    image =  Image.open(url)
    por = vqa_pipeline(image, question, top_k=k)
    os.system("cls")
    return por