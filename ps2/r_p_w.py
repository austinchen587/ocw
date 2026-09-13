from hangman import choose_word,wordlist
import string



secret_word = choose_word(wordlist)
letters_guessed_times = 10
letter_list = string.ascii_lowercase
letters_guessed = []


def has_player_won(secret_word, letters_guessed):

    print("Welcome to Hangman !")
    print(f"I am thinking of a word that is {len(secret_word)} letters long. ")

    while letters_guessed_times > 0:
        print("-" * 20)
        print(f"You have {letters_guessed_times} guesses left.")
        print(f"Available letters : {letter_list}")
        letters_guessed = input(f"please guess a letter:")

        if type(letters_guessed) != string or len(letters_guessed) != 1:
            print(f"pleas guess a letter from {letter_list} again")
        else:
            if letters_guessed not in secret_word:
                print("Oops! That letter is not in my word: ")
        



    


if __name__ == "__main__":
    pass