import pyttsx3
import random
import os

os.makedirs("audio_captchas",exist_ok=True)

engine = pyttsx3.init()

num_audio = 1000

for i in range(num_audio):
    text = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',k=6))
    
    audio_path = f"audio_captchas/{text}.mp3"
    
    engine.save_to_file(text,audio_path)
    engine.runAndWait()
    
    if i % 500 == 0:
        print(f"Generated {i} audios...")
        
        
print("Dataset Generated Successfully!")