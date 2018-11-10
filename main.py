import compression as cp

def main():
    file_name = 'sample_text_file.txt'
    file_compresser = cp.FileCompresser()
    
    file_compresser.read_file(file_name)
    phrases = file_compresser.encode()
    original_string = file_compresser.decode(phrases)
    print(phrases)
    print(original_string)

if __name__ == '__main__':
    main()
