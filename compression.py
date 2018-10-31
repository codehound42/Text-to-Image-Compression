
file_as_char_value_list = []
phrases = []
    
class Node:
    def __init__(self, phrase_num):
        self.phrase_num = phrase_num
        self.children = {}
    
    def add_child_node(self, child, edge_label):
        self.children[edge_label] = child
    
class LZ78Trie:
    current_phrase_number = 0
    p = 0
    
    def __init__(self):
        self.root = Node(0)
    
    def add_next_phrase(self):
        parent = None
        child = self.root
        current_char_value = None
        
        while child != None and LZ78Trie.p < len(file_as_char_value_list):
            parent = child
            current_char_value = file_as_char_value_list[LZ78Trie.p]
            child = parent.children.get(current_char_value)
            LZ78Trie.p += 1
        
        LZ78Trie.current_phrase_number += 1
        new_child_node = Node(LZ78Trie.current_phrase_number)
        parent.add_child_node(new_child_node, current_char_value)
        
        phrases.append((parent.phrase_num, current_char_value))
        

def read_file(file_name):
    with open(file_name, 'r') as fh:
        for line in fh:
            for c in line:
                file_as_char_value_list.append(c)
    
    #print(file_as_char_value_list)


# === Main ===

file_name = 'sample_text_file.txt'
read_file(file_name)
#file_as_char_value_list.append('$') # End of string

trie = LZ78Trie()
while trie.p < len(file_as_char_value_list):
    trie.add_next_phrase()

#print(trie.root.children)
print(phrases)





