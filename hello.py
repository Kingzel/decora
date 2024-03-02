import requests
from PIL import Image
from transformers import ViltProcessor, ViltForQuestionAnswering


image_url = "https://cdn.discordapp.com/attachments/1145006133879246931/1213135813421039646/ezgif-1-5d3305ee3c.jpg?ex=65f45fc4&is=65e1eac4&hm=c594555ac17a6d4e37c5e968e8a90da3afad9b1502a8172405d49483c6b7bf46&"
image = Image.open(requests.get(image_url, stream=True).raw)

model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

text = 'what is the vibe of this furniture'

encoding = processor(image, text, return_tensors="pt")
outputs = model(**encoding)
logits = outputs.logits

out=[]
for i in range(30):
    o = model.config.id2label[i]
    out.append(o)

print("Predicted answer:", out)