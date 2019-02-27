master_str = "hockey"

# It's in the air. Look at the letters.

english_dictionary_file = open("words_alpha.txt")
english_dictionary = english_dictionary_file.read().splitlines()

def fn_get_letters_dict(word):
    letters_dict = {}
    for letter in word:
        if letter in letters_dict.keys():
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1
    return letters_dict
    
def fn_compare_letters_dicts(sub_word, full_word):
    test_word = fn_get_letters_dict(sub_word)
    master_word = fn_get_letters_dict(full_word)
    
    for letter in test_word.keys():
        if letter not in master_word.keys():
            return False
        elif test_word[letter] > master_word[letter]:
            return False
    return True
    
new_words = [] 
    
for word in english_dictionary:
    if fn_compare_letters_dicts(word, master_str):
        new_words.append(word)
        
print(new_words)
    
    

