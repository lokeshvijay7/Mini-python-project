import random

User = 0
computer = 0
opsions = ["rock","paper","scissors"]
while True :
    user_input = input("Rock,Paper,Scissor or Q quit :").lower()
    computer_input = random.randint(0,2)
    computer_final = opsions[computer_input]
    if user_input == "q":
        break
    elif user_input == "rock" and computer_final == "scissors":
        print("You win")
        User += 1
    elif user_input == "paper" and computer_final == "rock":
        print("You win")
        User += 1
    elif user_input == "scissors" and computer_final == "paper":
        print("You win")
        User += 1
    else:
        print("computer wins")
        computer += 1

print(f"User wins : {User} Computer wins : {computer}")
print("Good bye")    