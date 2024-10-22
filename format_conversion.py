from text_compression import TextCompresser
import numpy as np
from PIL import Image

def int_to_rgb_values(val):
    red = (val >> 16) & 255
    green = (val >> 8) & 255
    blue = val & 255
    return red, green, blue

def rgb_values_to_int(red, green, blue):
    return blue + (green * 16**2) + (red * 16**4)
    
def read_image(file_path):
    img = Image.open(file_path)
    img_rgb = img.convert('RGB')
    
    width, height = img.size
    phrases = []
    
    for i in range(height):
        for j in range(0,width,2):
            red1, green1, blue1 = img_rgb.getpixel((j, i))
            red2, green2, blue2 = img_rgb.getpixel((j+1, i))
            
            phrase_pointer = rgb_values_to_int(red1, green1, blue1)
            char = chr(rgb_values_to_int(red2, green2, blue2))
            phrases.append((phrase_pointer, char))
    
    #print(phrases)
    return phrases

def render_image(file_path, phrases):
    height = int(np.sqrt(len(phrases)))
    width = 2*height
    
    current_phrase_index = 0
    pixels = list()
    for i in range(height):
        for j in range(0,width,2):            
            phrase_pointer = phrases[current_phrase_index][0]
            char_val = ord(phrases[current_phrase_index][1])
            
            red1, green1, blue1 = int_to_rgb_values(phrase_pointer)
            red2, green2, blue2 = int_to_rgb_values(char_val)
            
            pixels.append((red1, green1, blue1))
            pixels.append((red2, green2, blue2))
            
            current_phrase_index += 1
    
    #print(pixels)
    
    # Render image
    img = Image.new("RGB", (width,height))
    img.putdata(pixels)
    img.save(file_path)

def generate_compressed_image_file(text_file_name, image_file_name):
    file_compresser = TextCompresser()
    
    file_compresser.read_file(text_file_name)
    phrases = file_compresser.encode()
    
    render_image(image_file_name, phrases)
    print('done rendering')
    
    
def generate_orignal_text_file(image_file_name, text_file_name):
    file_compresser = TextCompresser()
    
    phrases = read_image(image_file_name)
    print('done reading image')
    
    original_string = file_compresser.decode(phrases)
    file = open(text_file_name, 'w') # Create a file if it does not already exist
    file.write(original_string)
    print('done writing to text file')
    
    