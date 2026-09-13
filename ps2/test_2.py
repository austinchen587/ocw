import string

letters =string.ascii_lowercase

word = "apple"

for i in word:
    if i not in letters:
        letters = letters
    else:
        letters = letters.replace(i,"")

print(letters)