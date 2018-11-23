import sys
from format_conversion import generate_orignal_text_file

def main():
    arguments = sys.argv
    
    script_name = arguments[0]
    image_file_name = arguments[1] # Input
    text_file_name = arguments[2] # Output
    
    print('Converting image "{}" to text file {}'.format(image_file_name, text_file_name))
    generate_orignal_text_file(image_file_name, text_file_name)
    print('Done')

if __name__ == '__main__':
    main()