import random

# 🎮 ASCII art for each choice
rock_ascii = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper_ascii = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors_ascii = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# 🤔 User choice
choice_user = input("Enter your choice (rock, paper, scissors): ").lower()
if choice_user not in ["rock", "paper", "scissors"]:
    print("Invalid choice! Please choose rock, paper, or scissors.")
    exit()

# 🧍‍♂️ Display user choice
if choice_user == "rock":
    print(f"\nYou chose:\n{rock_ascii}")
elif choice_user == "paper":
    print(f"\nYou chose:\n{paper_ascii}")
else:
    print(f"\nYou chose:\n{scissors_ascii}")


# 💻 Computer choice
choice_computer = random.choice(["rock", "paper", "scissors"])
if choice_computer == "rock":
    print(f"\nComputer chose:\n{rock_ascii}")
elif choice_computer == "paper":
    print(f"\nComputer chose:\n{paper_ascii}")
else:
    print(f"\nComputer chose:\n{scissors_ascii}")

# 🏆 Determine the winner
if choice_user == choice_computer:
    print("🤝 It's a Draw!")
elif (
    choice_user == "rock" and choice_computer == "scissors" or
    choice_user == "paper" and choice_computer == "rock" or
    choice_user == "scissors" and choice_computer == "paper"
):
    print("🎉 You win!")
else:
    print("😞 You lost!")

    
