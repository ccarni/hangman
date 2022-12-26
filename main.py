import random
import words_list as list_words

board_states = {
        0:  """
___ 
|   |
|
|
|""",
        1:  """
___
|   |
|   O
|
|""",
        2:  """
___
|   |
|   O
|   |
|""",
        3:  """
___
|   |
|   O
|   |
|  /""",
        4:  """
___
|   |
|   O
|   |
|  /\\""",
        5:  """
___
|   |
|  _O
|   |
|  /\\""",
        6:  """
___
|   |
|  _O_
|   |
|  /\\""",
    }
board = board_states[0]
word = random.choice(list_words.list_of_words).upper()

player_lost = False
guessed_letters = "_" * len(word)
guesses_num = 0
incorrect_guesses = 6

def get_input():
    try:
        global guesses_num
        global incorrect_guesses
        global guessed_letters
        global player_lost

        guess = input("Guess a letter: ")
        guesses_num += 1
        previous_guessed_letters = guessed_letters
        print(previous_guessed_letters)
        guessed_letters = ""

        for i in range(len(word)):
            if word[i] == guess.upper() or word[i] == previous_guessed_letters[i]:
                guessed_letters += word[i]
            else:
                guessed_letters += "_"
        if guessed_letters == previous_guessed_letters:
            incorrect_guesses -= 1

        if incorrect_guesses <= 0:
            player_lost = True 
    except:
        print("error in get_input")

def display_board():
    try:
        board = board_states[6 - incorrect_guesses]
        print(board)
        print(guessed_letters)
    except:
        print("error in display_board")

    

def end_game():
    try:
        if player_lost == True:
            print("You Ran Out of Guesses, The Word Was " + word)
        else:
            print("You guessed the word in " + str(guesses_num) + " Guesses.")
    except:
        print("error in end_game()")

def play():
    try:
        display_board()
        while player_lost == False and not guessed_letters == word:
            get_input()
            display_board()
        end_game()
    except:
        print("error in play()")

play()
