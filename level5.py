#peak hell
#pickle

import pickle

#not sure what to pickle or do with it?

raw_text = open('banner.p', 'rb')

new_text = pickle.load(raw_text)
raw_text.close()

print(len(new_text))
full_text = ''

for line in new_text:
    line_string = ''
    for tup in line:
        line_string += tup[0] * int(tup[1])
    full_text += line_string + '\n'
    
print(full_text)

new_file = open("level5_results.txt", "w+")
new_file.write(full_text)
