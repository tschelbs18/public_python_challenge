# Python Challenge Level 1

# Rules
# K -> M
# O -> Q
# E -> G

# Additional solution stuff
from tkinter import messagebox

input_txt = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

#~ input_txt.replace('k', 'm')
#~ input_txt.replace('o', 'q')
#~ input_txt.replace('e', 'g')

input_list = list(input_txt)
count = 0

url_txt = "http://www.pythonchallenge.com/pc/def/map.html"
url_list = list(url_txt)
url_count = 0

for letter in input_list:
    if ord(letter) >= 97 and ord(letter) <= 120:
        new_ascii = ord(letter) + 2
        new_letter = chr(new_ascii)
        input_list[count] = new_letter
    elif ord(letter) == 121:
        new_ascii = 97
        new_letter = chr(new_ascii)
        input_list[count] = new_letter
    elif ord(letter) == 122:
        new_ascii = 98
        new_letter = chr(new_ascii)
        input_list[count] = new_letter
    count = count + 1
    
for letter in url_list:
    if ord(letter) >= 97 and ord(letter) <= 120:
        new_ascii = ord(letter) + 2
        new_letter = chr(new_ascii)
        url_list[url_count] = new_letter
    elif ord(letter) == 121:
        new_ascii = 97
        new_letter = chr(new_ascii)
        url_list[url_count] = new_letter
    elif ord(letter) == 122:
        new_ascii = 98
        new_letter = chr(new_ascii)
        url_list[url_count] = new_letter
    url_count = url_count + 1

result_txt = "".join(input_list)    
result_url_txt = "".join(url_list)

print(result_txt)
print(result_url_txt)

messagebox.showinfo("URL", result_url_txt)

#OCR only that part of the URL needs ot change

