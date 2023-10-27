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

# Write your code below this line 👇
import random

game = [rock, paper, scissors]
print("Enter your choice? Type 0 for rock, 1 for paper, 2 for Scissors. \n")
user_choice = int(input("User Choice: "))
print(game[user_choice])

comp = len(game)
comp_choice = random.randint(0, comp - 1)

print(f"Computer choice: {comp_choice}")
print(game[comp_choice])

# //0(r):1(p)=p, 0(r):2=r, 1(p):0(r)=p, 1(p):2=s, 2:0(r)=r, 2:1(p)=s

if user_choice == 0 and comp_choice == 1:
    print("Computer wins!! (Paper beats Rock).")
    print("You Lose.")

elif user_choice == 0 and comp_choice == 2:
    print("You win!!")

elif user_choice == 1 and comp_choice == 0:
    print("You win!!")

elif user_choice == 1 and comp_choice == 2:
    print("Computer wins!! (Scissors beats Paper)")
    print("You Lose.")

elif user_choice == 2 and comp_choice == 0:
    print("Computer wins!! (Rock beats Scissors)")
    print("You Lose.")

elif user_choice == 2 and comp_choice == 1:
    print("You win!!")

else:
    print("It's Draw...")
