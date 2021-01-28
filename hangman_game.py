logo = """
╦ ╦┌─┐┌┐┌┌─┐┌┬┐┌─┐┌┐┌
╠═╣├─┤││││ ┬│││├─┤│││
╩ ╩┴ ┴┘└┘└─┘┴ ┴┴ ┴┘└┘
"""

win = """
╦ ╦╔═╗╦ ╦  ╦ ╦╦╔╗╔  ┬┬
╚╦╝║ ║║ ║  ║║║║║║║  ││
 ╩ ╚═╝╚═╝  ╚╩╝╩╝╚╝  oo
 """

game_over = """
╔═╗┌─┐┌┬┐┌─┐  ┌─┐┬  ┬┌─┐┬─┐
║ ╦├─┤│││├┤   │ │└┐┌┘├┤ ├┬┘
╚═╝┴ ┴┴ ┴└─┘  └─┘ └┘ └─┘┴└─
"""


import hangman
import requests
import time

# number of wrong inputs
n = 0

# initializing hangman
hm = hangman.hangman(0)

# initializing word
word = ""

# initializing guessed word list
guessed_word = []

# initializing guessed letter list
guessed_letters = []

def get_random_word():
    '''
    Generates a random word from api
    '''
    url = "https://random-word-api.herokuapp.com/word?number=1"
    while True:
        print("Getting a random word...")
        response = requests.get(url)
        if response.status_code != 200:
            print("Just a second...")
            time.sleep(2)
        else:
            break
    return response.text[2:-2]

def print_hangman():
    '''
    Prints the hangman
    '''

    print()

    print()

    for i in hm:
        print(f'| {" ".join(i).center(18)}')

def print_word():
    '''
    Prints the guessed word
    '''
    print()
    print(f'Word : {" ".join(guessed_word)}')
    print()

def fill_guessed_word(letter):
    '''
    Fills the letter guessed in the guessed word and returns True if letter exists in word else False
    '''

    # if the letter is not in word, return False
    if letter not in word:
        return False

    # filling the guessed word with the letter
    for i in range(len(word)):
        if word[i] == letter:
            guessed_word[i] = letter

    return True


def end_game(w):
    global win, game_over, word
    print()

    # if user wins
    if w == True:
        print(win)
    else:
        print(f"The word was : {word}")
        print(game_over)
    
def game():
    '''
    Main Game
    '''

    global logo, n, hm, word, guessed_word
    print(logo)

    # randomly generated word
    word = get_random_word()

    # initialize empty word
    guessed_word = ["_" for i in range(len(word))]

    print_word()

    while n < 6:
        print(f"The letters you have guessed till now : {guessed_letters}")
        
        # guessed letter 
        l = input("Enter a letter you would like to guess : ")
        
        if l in guessed_letters:
            print("")


        # try to fill the letter in the guessed word
        fill = fill_guessed_word(l)
        
        # if the letter doesnt exist in the word, update the hangman
        if not fill:
            n += 1
            hm = hangman.hangman(n)
            print_hangman()
        


        # update the guessed letters list
        guessed_letters.append(l)

        # print the word
        print_word()

        # if the word is fully guessed right
        if ''.join(guessed_word) == word:
            end_game(True)
            break
    else:
        end_game(False)

    print()
    print()


if __name__=="__main__":
    while True:
        game()
        c = input("\nWould you like to play again ? (Y/N) : ")
        if c == "y" or c == "Y":
            continue
        else:
            break
        