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
    print("Welcome to Hangman! ")
    vowels = ['a', 'e', 'i', 'o', 'u']

    print(f"I am thinking of a word that is {len(secret_word)} letters long.")

    while time > 0 :
        alphabetical = get_available_letters(letters_guessed)
        string = get_word_progress(secret_word,letters_guessed)

        print("-" * 60)

        print(f"Available letters : {alphabetical}")
        print(f"You have {time} guesses left. ")
        letter = input("Enter an letter: ")

        if with_help and letter == "!":
            if time < 3:
                print("Oops! Not enough guesses left to use help.")
                continue

            unrevealed = [ch for ch in secret_word if ch not in letters_guessed]
            if unrevealed:
                chosen = random.choice(unrevealed)
                letters_guessed += chosen
                time -= 3

                string = get_word_progress(secret_word,letters_guessed)
                print(f"Letter revealed: {chosen}")


                if has_player_won(secret_word,letters_guessed):
                    print("Congratulations, you won!")
                    print(f"Your total socre for this game is : {(time+4*len(set(secret_word)))+(3+len(secret_word))}")
                    return
            continue

        while letter not in alphabetical:
            print(f"Oops! That is not valid letter. Please input a letter from : {alphabetical}")
            print("-" * 60)
            print(f"You have {time} guesses left. ")
            letter = input("Enter an letter: ")
            if with_help and letter == "!":
                break

        if letter == "!":
            continue


        letters_guessed += letter
        string = get_word_progress(secret_word,letters_guessed)


        if letter not in secret_word:
            print(f"Oops! That letter is not in my word: {string}")
            if letter not in vowels :
                time -= 1
            else:
                time -= 2
        else:
            print(f"Good guess: {string}")
            if has_player_won(secret_word,letters_guessed):
                print("Congratulations, you won!")
                print(f"Your total socre for this game is : {(time+4*len(set(secret_word)))+(3+len(secret_word))}")
                return

    print(f"Sorry, you ran out of guesses. The word was {secret_word}.")


           

        

if __name__ == "__main__":
    #secret_word = choose_word(wordlist)
    secret_word = "apple"

    #letters_guessed = []
    #time = 10
    with_help = True
    
    hangman(secret_word,with_help)