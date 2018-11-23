    
class Node:
    
    def __init__(self, phrase_num):
        self.phrase_num = phrase_num
        self.children = {}
    
    def add_child_node(self, child, edge_label):
        self.children[edge_label] = child
    
class LZ78Trie:
    
    def __init__(self):
        self.root = Node(0)
    
    def add_next_phrase(self, phrases, current_phrase_number, p, char_list):
        node = self.root
        
        # Search through trie
        # Builds up next phrase until leaf node reached
        while node != None and p < len(char_list):
            parent = node
            current_char_value = char_list[p]
            node = parent.children.get(current_char_value)
            p += 1
        
        new_child_node = Node(current_phrase_number)
        parent.add_child_node(new_child_node, current_char_value)
        
        phrases.append((parent.phrase_num, current_char_value))
        
        return p
        
    def generate_phrases(self, char_list):
        phrases = []
        p = 0
        current_phrase_number = 0
        
        # Generate phrases for entire string
        while p < len(char_list):
            current_phrase_number += 1
            p = self.add_next_phrase(phrases, current_phrase_number, p, char_list)
            #print("next phrase, p: {}".format(p))
            
        return phrases
        
class TextCompresser:
    
    def __init__(self):
        self.trie = LZ78Trie()
        self.file_as_char_value_list = []
    
    def read_file(self, file_name):
        with open(file_name, 'r', encoding="utf8") as fh:
            for line in fh:
                #print(line)
                for c in line:
                    self.file_as_char_value_list.append(c)
        return self.file_as_char_value_list
    
    def encode(self):
        self.phrases = self.trie.generate_phrases(self.file_as_char_value_list)
        return self.phrases
    
    def decode(self, phrases):
        phrases_as_strings = ['']
        p = 0
        
        # Read phrases left to right and generate segments of original string
        while p < len(phrases):
            phrase = phrases[p]
            
            phrase_pointer = phrase[0]
            char = phrase[1]
            
            previous_string_copy = phrases_as_strings[phrase_pointer]
            phrases_as_strings.append(previous_string_copy + char)
            
            p += 1
        
        # Return concatenated string segments
        return ''.join(phrases_as_strings)

