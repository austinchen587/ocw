import string
import random


file = r"/Users/austinchen587gmail.com/myenv/ocw/ps2/words.txt"
with open(file,"r") as f :
    word = random.choice(f.read().split())
letter_list = ""
letter_guess = ""
time = 10
letter_ascii = string.ascii_lowercase

#word ="apple"

while time>0:
    print("-" * 60)
    print(f'I am thinking of a word that is {len(word)} letters long. ')
    print(f'Available letters : {letter_ascii}')
    print(f"you have {time} time left.")
    letter = input("Enter an letter:")


    while letter not in letter_ascii:
        print(f"Oops! That is not valid letter. Please input a letter from : {letter_ascii}")
        letter = input("Enter an letter:")

    letter_list = letter_list + letter
    for i in letter_list:
        letter_ascii = letter_ascii.replace(i,"")


    for i in range(len(word)):
        if word[i] not in letter_list:
            letter_guess = letter_guess + "*"           
        else:
            letter_guess = letter_guess + word[i]

    if letter not in word:
        print(f'Oops! That letter is not in my word: {letter_guess}')
        time -= 1
    else:
        print(f"Good guess: {letter_guess}") 

    letter_guess = ""   
    print(letter_list)

print(f"the secret word: {word}")      

    





