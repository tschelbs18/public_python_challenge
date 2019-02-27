
raw_text = open('level3_mess.txt')
# Saved mess text to text file for easier access

for line in raw_text:
    row = str(line).replace("\n", '')
    for x in range(0,len(row)-8):
        left = row[x]
        body1 = row[x+1:x+4]
        mid = row[x + 4]
        body2 = row[x+5:x+8]
        right = row[x+8]
        if body1 == body1.upper() and mid == mid.lower() and  body2 == body2.upper() and left == left.lower() and right == right.lower():
            print(left+ body1 + mid + body2 + right)
            
