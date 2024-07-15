from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np


text = 'text to convert to signature'

def text_to_image(text):

    #Pick font on your local stored fonts or you can download ttf or otf files.
    font_path = r'C:\Windows\fonts\BRUSHSCI.TTF'
    font_size = 40
    font = ImageFont.truetype(font_path, font_size)

    bbox = font.getbbox(text)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Create image with white background
    image = Image.new('RGB', (text_width + 50, text_height + 50), color='white')

    # Initialize the drawing context
    draw = ImageDraw.Draw(image)

    # position at which to draw the text
    x = (image.width - text_width) / 1.5
    y = (image.height - text_height) / 3

    # Draw the text onto the image
    draw.text((x, y), text, font=font, fill='black')

    # Save the image
    image.save(f'{text}.png')
    
    file_name = f'{text}.png' 

    #converting to transparent background
    final_image = cv2.imread(file_name, 1)
    final_image = cv2.cvtColor(final_image, cv2.COLOR_BGR2RGBA)
    final_image[np.all(final_image == [255, 255, 255, 255], axis=2)] = [0, 0, 0, 0]

    cv2.imwrite(rf"file_path\final_image_{text}.png", final_image) #create your own file path.

text_to_image(text)