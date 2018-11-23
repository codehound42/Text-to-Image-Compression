import sys
from format_conversion import generate_compressed_image_file

def main():
    arguments = sys.argv
    
    script_name = arguments[0]
    text_file_name = arguments[1] # Input
    image_file_name = arguments[2] # Output
    
    print('Converting text file "{}" to image {}'.format(text_file_name, image_file_name))
    generate_compressed_image_file(text_file_name, image_file_name)
    print('Done')

if __name__ == '__main__':
    main()