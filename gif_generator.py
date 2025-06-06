# Gif Generator
from PIL import Image
import imageio
import os
import numpy as np

'''image = Image.open("wallpaper 2.jpg")
image.show()
resized = image.resize((300,300))
resized.save("resized_sample.jpg")
#resized.show()'''

# converting all images to RGB color (3 channels)
def generate_gif(input_folder, output_path, duration=0.5,size=(300,300)):
    frames=[]
    # Sort the images aplhabetically 
    for filename in sorted(os.listdir(input_folder)): 
        if filename.endswith((".png",".jpg",".jpeg")):
            path = os.path.join(input_folder, filename)
            img=Image.open(path).convert("RGB")
            img = img.resize(size)
            
            # Right now list is used for recording the images
            # the dimensions of the images should be same
            # No grayscale, no alpha channel, no mismatches → no error
            frame=np.array(img)
            frames.append(frame)

        if not frames:
            print("No vaid images found.")
            return

    imageio.mimsave(output_path, frames, duration=duration)
    print(f"GIF saved to: {output_path}'")

generate_gif("images","output.gif",duration=1.0)