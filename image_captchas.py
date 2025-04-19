import os
from captcha.image import ImageCaptcha
import random

os.makedirs("captchas",exist_ok=True)

image = ImageCaptcha(width = 200,height = 90,
                     fonts = ["arial.ttf","comic.ttf"],
                     font_sizes = [40,50,60])


num_images = 1000

for i in range(num_images):
    text = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",k=6))
    
    image_path = f"captchas/{text}.png"
    image.write(text,image_path)
    
    if i % 500 == 0:
        print(f"Generated {i} images...")
        
        
print("Dataset Generated Successfully")