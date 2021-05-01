def man(turns):
    if turns == 9:
        print("9 turns left")
        print("  --------  ")
    if turns == 8:
        print("8 turns left")
        print("  --------  ")
        print("     O      ")
    if turns == 7:
        print("7 turns left")
        print("  --------  ")
        print("     O      ")
        print("     |      ")
    if turns == 6:
        print("6 turns left")
        print("  --------  ")
        print("     O      ")
        print("     |      ")
        print("    /       ")
    if turns == 5:
        print("5 turns left")
        print("  --------  ")
        print("     O      ")
        print("     |      ")
        print("    / \     ")
    if turns == 4:
        print("4 turns left")
        print("  --------  ")
        print("   \ O      ")
        print("     |      ")
        print("    / \     ")
    if turns == 3:
        print("3 turns left")
        print("  --------  ")
        print("   \ O /    ")
        print("     |      ")
        print("    / \     ")
    if turns == 2:
        print("2 turns left")
        print("  --------  ")
        print("   \ O /|   ")
        print("     |      ")
        print("    / \     ")
    if turns == 1:
        print("1 turns left")
        print("Last breaths counting, Take care!")
        print("  --------  ")
        print("   \ O_|/   ")
        print("     |      ")
        print("    / \     ")
    if turns == 0:
        print("You loose")
        print("You let a kind man die")
        print("  --------  ")
        print("     O_|    ")
        print("    /|\      ")
        print("    / \     ")

def interface():
    print("*****WELCOME*****")
    print("-----------------")
    print("***HANGMAN GAME**")
    print("Guess the Word in less than 10 turns")

import random
list=["burger" , "batman" , "tiger" , "superman" , "thor" , "pokemon" , "avengers" , "savewater" , "earth" , "annable"]
word=random.choice(list)
guessword=""
turns=10
guessmade=""

for letter in word:
    guessword=guessword+"_"+" "
interface()

while turns>0 and guessword!=word:
    print("Guess The Word",guessword)
    guess=input()
    if guess in word:
        guessmade=guessmade+guess
        guessword=""
        for letter in word:
            if letter in guessmade:
                guessword=guessword+letter
            else:
                guessword=guessword+"_"+" "

    else:
        turns=turns-1
        man(turns)
if(turns>0):
    print("%s \n YOU WIN"%guessword)
