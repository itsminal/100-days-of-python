import random

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
l = [rock, paper, scissors]
uchoice = int(input())

if uchoice == 0:
    print(l[0])
elif uchoice == 1:
    print(l[1])
elif uchoice == 2:
    print(l[2])

print("Computer chose: ")
comp = random.randint(0, 2)
print(l[comp])

if uchoice == comp:
    print("It's a draw")
elif uchoice == 0:
    if comp == 1:
        print("Computer wins!")
    elif comp == 2:
        print("You win!")
elif uchoice == 1:
    if comp == 2:
        print("Computer wins!")
    elif comp == 0:
        print("You win!")
elif uchoice == 2:
    if comp == 0:
        print("Computer wins!")
    elif comp == 1:
        print("You win!")
