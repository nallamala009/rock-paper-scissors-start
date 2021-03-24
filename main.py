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

user_input = int(input("Type 0 for Rock, 1 for Scissor and 2 for Paper"))
images = [rock, paper, scissors]
computer_input = random.randint(0 , 2)
if user_input == "1" and computer_input == "0":
  print(f"you choose {images[1]}\n computer choose {images[0]} \n you loose")
if user_input == "2" and computer_input == "0":
  print(f"you choose {images[2]}\n computer choose {images[0]} \n you won")
if user_input == "1" and computer_input == 2:
  print(f"you choose {images[1]}\n computer choose {images[2]} \n you loose")
if user_input == 0 and computer_input == 1:
  print(f"you choose {images[0]}\n computer choose {images[1]} \n you won")
else:
  print(f"you choose {images[user_input]}\n computer choose {images[computer_input]} \n its a draw")
