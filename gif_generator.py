# Gif Generator
from PIL import Image,ImageDraw
import imageio
import os
import numpy as np
import webbrowser

'''image = Image.open("wallpaper 2.jpg")
image.show()
resized = image.resize((300,300))
resized.save("resized_sample.jpg")
#resized.show()'''

# converting all images to RGB color (3 channels)
def generate_gif(input_folder, output_path, duration=0.5,size=(300,300)):
    frames=[]
    # Sort the images aplhabetically
    # # Right now list is used for recording the images 
    # the dimensions of the images should be same
    for filename in sorted(os.listdir(input_folder)): 
        if filename.endswith((".png",".jpg",".jpeg")):
            path = os.path.join(input_folder, filename)
            # Open image and convert to RGB mode
            img=Image.open(path).convert("RGB")
            img = img.resize(size)
            
            # labelling image
           ''' draw = ImageDraw.Draw(img)
            draw.text((10,10),f'Frame {len(frames)+1}', fill=(255,255,255))
            # No grayscale, no alpha channel, no mismatches → no error'''

            frame=np.array(img)
            frames.append(frame)

    if not frames:
        print("No vaid images found.")
        return

    imageio.mimsave(output_path, frames, duration=duration)
    print(f"GIF saved to: {output_path}'")

    #Accessing default image viewer
    abs_path = os.path.abspath(output_path)
    webbrowser.open(f'file://{abs_path}')

generate_gif("images","output.gif",duration=5.0)




