# Channel
# Channel.zip file thanks to the zipper

# Zip file contains text file with the same old "nothing" prompts
# Also the readme says to start at 90052 and that the answer is inside the zip

# Loop through all the text files in the zip and stop when one doesn't say 
# and the next nothing is

import os
from zipfile import ZipFile

    
zip_path = r"channel.zip"
myzip = ZipFile(zip_path)

initial_file = "90052"
first = myzip.open(initial_file + ".txt", mode ='r')
text = (first.read().decode('utf-8'))
next = text[16:]

solved = False
comments = []

while not(solved):
    if "nothing" not in text:
        solved = True
    else:
        file = myzip.open(next + ".txt", mode ='r')
        comment = myzip.getinfo(next + ".txt").comment.decode('utf-8')
        comments.append(comment)
        text = file.read().decode('utf-8')
        next = text[16:]
    

print("".join(comments))
# Hockey
