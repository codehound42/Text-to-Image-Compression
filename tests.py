import unittest
from text_compression import TextCompresser
from format_conversion import render_image, read_image

class TestCompression(unittest.TestCase):
    
    def test_phrases(self):
        text_compresser = TextCompresser()
        file_path = 'text_files/test_phrases.txt'
        
        text_compresser.read_file(file_path)
        
        phrases = text_compresser.encode()
        expected_phrases = [(0, 'a'), (0, 'b'), (0, 'c'), (1, 'b'), (3, 'a'), (2, 'a'), (6, 'c'), (4, 'a'), (2, 'c')]
        self.assertEqual(phrases, expected_phrases)
        
    def test_encode_decode(self):
        text_compresser = TextCompresser()
        text_file_path = 'text_files/sample_text_file.txt'
        image_file_path = 'image_files/sample_text_file_out.png'
        file_as_char_value_list = text_compresser.read_file(text_file_path)
        
        original_string = ''.join(file_as_char_value_list)
        print(original_string)
        
        original_phrases = text_compresser.encode()
        print('done encoding')
        render_image(image_file_path, original_phrases)
        print('done rendering')
        phrases_from_image = read_image(image_file_path)
        print('done reading image')
        decoded_string = text_compresser.decode(phrases_from_image)
        print('done decoding phrases')
        
        # Compare phrases before and after
        # These are likely not of the same length, since some pixels in the image are not used
        self.assert_(len(phrases_from_image) <= len(original_phrases))
        p = 0
        for (phrase_pointer1, char1) in phrases_from_image:
            (phrase_pointer2, char2) = original_phrases[p]
            self.assertEqual(phrase_pointer1, phrase_pointer2)
            self.assertEqual(char1, char2)
            p += 1
        
        # Compare original string with the one encoded and then decoded
        self.assertEqual(original_string, decoded_string)
        
if __name__ == '__main__':
    unittest.main()
        