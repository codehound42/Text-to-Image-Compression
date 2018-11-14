import compression as cp
import numpy as np
from PIL import Image

def int_to_rgb_values(val):
    red = (val >> 16) & 255
    green = (val >> 8) & 255
    blue = val & 255
    return red, green, blue

def render_image(phrases):
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
    
    print(pixels)
    
    # Render image
    img = Image.new("RGB", (width,height))
    img.putdata(pixels)
    img.save("test.png")
    
    print('done rendering')
    
def main():
    file_name = 'sample_text_file.txt'
    file_compresser = cp.FileCompresser()
    
    file_compresser.read_file(file_name)
    phrases = file_compresser.encode()
    original_string = file_compresser.decode(phrases)
    print(phrases)
    print(original_string)
    
    render_image(phrases)
    #test()

if __name__ == '__main__':
    main()
