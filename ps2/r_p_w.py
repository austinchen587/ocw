from hangman import choose_word,wordlist,string
import random



def has_player_won(secret_word, letter_guessed):

    for i in secret_word:
        if i not in letter_guessed:
            return False

    return True


#print(word_test)
#print(has_player_won(word_test,letters_guessed))

def get_word_progress(secret_word, letters_guessed):

    string = ''

    for i in secret_word:
        if i in letters_guessed:
            string += i
        else:
            string += "*"

    return string

#print(get_word_progress(word_test,letters_guessed))


def get_available_letters(letters_guessed):

    alphabetical = string.ascii_lowercase



    for i in letters_guessed:
        if i in alphabetical:
            alphabetical = alphabetical.replace(i,"")

    return alphabetical

#print(get_available_letters(letters_guessed))


def hangman(secret_word, with_help):
    time = 10
    letters_guessed = ""
    alphabetical = get_available_letters(letters_guessed)
    string = get_word_progress(secret_word,letters_guessed)
    letter_help = ""

    print("Welcome to Hangman!")
 
    print(f'I am thinking of a word that is {len(secret_word)} letters long. ')

    while time>0:
        print("-" * 60)
        
        print(f'Available letters : {alphabetical}')
        print(f"You have {time} guesses left.")
        letter = input("Enter an letter: ")

        while letter not in alphabetical:
            if letter != "!":
                print(f"Oops! That is not valid letter. Please input a letter from : {alphabetical}")
                letter = input("Enter an letter:") 
            else:
                for n in secret_word:
                    if n not in string:
                        letter_help += n 

                letters_guessed = letters_guessed + random.choice(letter_help)
                alphabetical = get_available_letters(letters_guessed)
                string = get_word_progress(secret_word,letters_guessed)
                print(f"Letter revealed: {string}")


        letters_guessed = letters_guessed + letter
        string = get_word_progress(secret_word,letters_guessed)

        alphabetical = get_available_letters(letters_guessed)

        if letter not in secret_word:
            print(f'Oops! That letter is not in my word: {string}')
            time -= 1
        else:
            print(f"Good guess: {string}")
            if has_player_won(secret_word,letters_guessed):
                print("Congratulations, you won!")
                break

    print(f"Sorry, you ran out of guesses. The word was {secret_word}.")


        

if __name__ == "__main__":
    secret_word = "ad"
    #letters_guessed = []
    #time = 10
    
    hangman(secret_word)