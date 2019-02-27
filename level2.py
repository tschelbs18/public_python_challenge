#~ from urllib.request import urlopen

#~ url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
#~ page = urlopen(url)
#~ html = page.read()

#~ print(html)

# Code for pulling html doesn't work perfectly

raw_text = open('level2_mess.txt')
# Saved mess text to text file for easier access
characters = []
char_counts = []
New = False

for line in raw_text:
    row = str(line).replace("\n", '')
    for x in range(0,len(row)):
        character = row[x]
        if character in characters:
            char_counts[characters.index(character)] = char_counts[characters.index(character)] + 1
        else:
            characters.append(character)
            char_counts.append(1)
            
for x in range(0,len(characters)):
    print(str(characters[x]) + ': ' + str(char_counts[x]))
