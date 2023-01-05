import random
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

#Write your code below this line 👇

game = [rock,paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
message = ""
if user_choice >= 0 and user_choice <=2:
   
    print(game[user_choice])
    computer_choice = random.randint(0, len(game)-1)
    print(f"Computer Choice:\n {game[computer_choice]}")
    if user_choice == 0 and  computer_choice == 2:
        message = "You win!"
    elif user_choice == 2 and computer_choice == 1:
        message = "You win!"
    elif user_choice == 1  and computer_choice == 0:
        message = "You win!"
    elif user_choice == computer_choice:
        message = "It's draw!"
    else :
        message = "You lose!"
else:
    message = "not a valid input"

print(message)