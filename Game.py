# random integer
from random import randint

# list for weapon
WEAPON = ["Rock", "Paper", "Scissors"]

# module to run the program
#def main():
#    menu()

def main():
menuSelect = ""
print("\tRock, Paper, Scissors!")

# main menu
print("\n\t\tMain Menu")
print("\t1. See the rules")
print("\t2. Play against the computer")
print("\t3. Play a two player game")
print("\t4. Quit")

menuSelect = int(input("\nPlease select one of the four options "))

while menuSelect < 1 or menuSelect > 4:
    print("The selection provided is invalid.")
    menuSelect = int(input("\nPlease select one of the four options "))

if menuSelect == 1:
    rules()
elif menuSelect == 2:
    onePlayer()
elif menuSelect == 3:
    twoPlayer()
elif menuSelect == 4:
    endGame()

# display the rules to the user
def rules():

print("\n\t\tRules")
print("\tThe game is simple:")
print("\tPaper Covers Rock")
print("\tRock Smashes Scissors")
print("\tScissors Cut Paper")
print("")

# one player mode
def onePlayer():
again = ""
player = False

print("\n\tPlayer VS Computer")

while player == False:
    player = input("\nSelect your weapon: Rock, Paper, or Scissors\n")
    player = player.lower()

    computer = WEAPON[randint(0,2)]
    computer = computer.lower()

    if player == computer:
        print(player," vs ",computer)
        print("It's a tie!\n")
    elif player == "rock":
        if computer == "paper":
            print(player," vs ",computer)
            print("Paper covers rock! You lose!\n")
        else:
            print("Rock smashes",computer,". You win!\n")     
    elif player == "paper":
        if computer == "scissors":
            print(player," vs ",computer)
            print("Scissors cut paper! You lose!\n")
        else:
            print("Paper covers",computer,". You win!\n")
    elif player == "scissors":
        if computer == "rock":
            print(player," vs ",computer)
            print("Rock smashes scissors! You lose!\n")
        else:
            print("Scissors cut",computer,". You win!\n")
    else:
        print("invalid input")

    again = input("Would you like to play again? Yes or no\n")
    again = again.lower()

    if again == "yes" or "y":
        player = False
    elif again == "no" or "n":
        main()


# two player mode
def twoPlayer():
fight = False
player1 = ""
player2 = ""

print("\n\tPlayer VS Player")

while fight == False:
    player1 = input("\nSelect your weapon: Rock, Paper, or Scissors\n")
    player1 = player1.lower()
    player2 = input("\nSelect your weapon: Rock, Paper, or Scissors\n")
    player2 = player2.lower()

    if player1 == player2:
        print(player1," vs ",player2)
        print("It's a tie!\n")
    elif player1 == "rock":
        if player2 == "paper":
            print(player1," vs ",player2)
            print("Paper covers rock! Player 2 wins!\n")
        else:
            print("Rock smashes",player2,". Player 1 wins!\n")     
    elif player1 == "paper":
        if player2 == "scissors":
            print(player1," vs ",player2)
            print("Scissors cut paper! Player 2 wins!\n")
        else:
            print("Paper covers",player2,". Player 1 wins!\n")
    elif player1 == "scissors":
        if player2 == "rock":
            print(player1," vs ",player2)
            print("Rock smashes scissors! Player 2 wins!\n")
        else:
            print("Scissors cut",player2,". Player 1 wins!\n")
    else:
        print("invalid input")

    again = input("Would you like to play again? Yes or no\n")
    again = again.lower()

    if again == "yes" or "y":
        player = False
    elif again == "no" or "n":
        main()

def endGame():
print("Thank you for playing!")

main()