import random

ls = ["rock", "paper", "scissors"]
name = input("Enter your name: ")
print(f"Hello {name}!!! Glad to see you here.\nIf you win 3 times against the computer, you will win.\nYou can answer only by writing rock, paper, or scissors.\nLet's begin the game. Good luck!")

marks = 0
cmarks = 0

while marks < 3 and cmarks < 3:
    l = random.choice(ls)
    scan = input("Enter your move: ").lower()
    
    if scan not in ls:
        print("Invalid move! Try again.")
        continue
    
    if l == scan:
        print("It's a tie!")
    elif (l == "rock" and scan == "scissors") or (l == "paper" and scan == "rock") or (l == "scissors" and scan == "paper"):
        print("Oh no, the computer won this round!")
        cmarks += 1
    else:
        print("Congratulations, you won this round!")
        marks += 1

if cmarks == 3:
    print("Computer won the game!")
else:
    print(f"Congratulations {name}, you won the game!")
import random

ls = ["rock", "paper", "scissors"]
name = input("Enter your name: ")
print(f"Hello {name}!!! Glad to see you here.\nIf you win 3 times against the computer, you will win.\nYou can answer only by writing rock, paper, or scissors.\nLet's begin the game. Good luck!")

marks = 0
cmarks = 0

while marks < 3 and cmarks < 3:
    l = random.choice(ls)
    scan = input("Enter your move: ").lower()
    
    if scan not in ls:
        print("Invalid move! Try again.")
        continue
    
    if l == scan:
        print("It's a tie!")
    elif (l == "rock" and scan == "scissors") or (l == "paper" and scan == "rock") or (l == "scissors" and scan == "paper"):
        print("Oh no, the computer won this round!")
        cmarks += 1
    else:
        print("Congratulations, you won this round!")
        marks += 1

if cmarks == 3:
    print("Computer won the game!")
else:
    print(f"Congratulations {name}, you won the game!")
import random

ls = ["rock", "paper", "scissors"]
name = input("Enter your name: ")
print(f"Hello {name}!!! Glad to see you here.\nIf you win 3 times against the computer, you will win.\nYou can answer only by writing rock, paper, or scissors.\nLet's begin the game. Good luck!")

marks = 0
cmarks = 0

while marks < 3 and cmarks < 3:
    l = random.choice(ls)
    scan = input("Enter your move: ").lower()
    
    if scan not in ls:
        print("Invalid move! Try again.")
        continue
    
    if l == scan:
        print("It's a tie!")
    elif (l == "rock" and scan == "scissors") or (l == "paper" and scan == "rock") or (l == "scissors" and scan == "paper"):
        print("Oh no, the computer won this round!")
        cmarks += 1
    else:
        print("Congratulations, you won this round!")
        marks += 1

if cmarks == 3:
    print("Computer won the game!")
else:
    print(f"Congratulations {name}, you won the game!")
