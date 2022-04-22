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
game_images = [rock, paper, scissors]
computerChoice = random.randint(0,2) 
userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if userChoice >= 3 or userChoice < 0: 
  print("You typed an invalid number, you lose!") 
elif userChoice == 0 and computerChoice == 2:
  print(game_images[userChoice])
  print("Computer chose:")
  print(game_images[computerChoice])
  print("You win!")
elif computerChoice == 0 and userChoice == 2:
  print(game_images[userChoice])
  print("Computer chose:")
  print(game_images[computerChoice])
  print("You lose")
elif computerChoice > userChoice:
  print(game_images[userChoice])
  print("Computer chose:")
  print(game_images[computerChoice])
  print("You lose")
elif userChoice > computerChoice:
  print(game_images[userChoice])
  print("Computer chose:")
  print(game_images[computerChoice])
  print("You win!")
elif computerChoice == userChoice:
  print(game_images[userChoice])
  print("Computer chose:")
  print(game_images[computerChoice])
  print("It's a draw")
