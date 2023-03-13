
rock = r'''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = r'''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = r'''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''  

import random

user_choice= int(input("Please choose 0 for rock, 1 for paper and 2 for scissor\n\n"))

if user_choice==0:
  print("You chose\n "+rock)
elif user_choice==1:
  print("You chose\n "+paper)
elif user_choice==2:
  print("You \n "+scissors)
  
  
inputs= [rock, paper, scissors]
random_computer_choice= random.randint(0,2)

print(f"the computer chose\n {inputs[random_computer_choice]}")

if user_choice==0 and random_computer_choice== 2:
  print("You win!")
elif user_choice== random_computer_choice:
  print("Its a draw!")
elif random_computer_choice > user_choice:
  print("You Lose!")
elif random_computer_choice == 0 and user_choice == 2:
  print("You lose!")
elif user_choice > random_computer_choice:
  print("You Win!")
else:
  print("Invalid Input, You Lose!")