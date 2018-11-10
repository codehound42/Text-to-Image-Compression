import compression as cp

def main():
    file_name = 'sample_text_file.txt'
    file_compresser = cp.FileCompresser()
    
    file_compresser.read_file(file_name)
    file_compresser.compress()
    print(file_compresser.phrases)

if __name__ == '__main__':
    main()
