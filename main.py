import compression as cp
import numpy as np
#import scipy.misc as smp
from PIL import Image

def render_image(phrases):
    height = int(np.sqrt(len(phrases)))
    width = 2*height
    
    
    current_phrase_index = 0
    pixels = np.zeros(height*width, dtype=np.uint8)
    for i in range(height):
        for j in range(0,width,2):
            if current_phrase_index >= len(phrases):
                break
            
            phrase_pointer = phrases[current_phrase_index][0]
            char_val = ord(phrases[current_phrase_index][1])
            
            pixels[i*width + j] = phrase_pointer
            pixels[i*width + j+1] = char_val
            
            current_phrase_index += 1
    
    # Render image
    new_im = Image.new("L", (width,height))
    new_im.putdata(pixels)
    new_im.save("test.png")
    #img.show()
    
    print('done rendering')
    

def test():
    w, h = 512, 512
    data = np.zeros((h, w, 3), dtype=np.uint8)
    data[256, 256] = [255, 0, 0]
    img = Image.fromarray(data, 'RGB')
    img.save('test.png')
    #img.show()
    
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
