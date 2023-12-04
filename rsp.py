import random

print(" ~~~~~~ Welcome to Rock Paper, Scissor Game ~~~~~~ ")

user_name = input("Enter Your Name: ")
print("😎 Hello, Mr.", user_name)

print("""
Game Rule..... 🏆🥳🤩🤓
1. Rock vs Paper = Paper win 📜
2. Rock vs Scissor = Rock win 👊
3. Paper vs Scissor = Scissor win ✌️
""")

game = ["Rock 👊", "Paper 📜", "Scissor ✌️"]

user_score = 0
computer_score = 0
ties = 0

while True:
    game_start = int(input("\n"
                           "    🎮 Game Start...\n"
                           "    1 Yes Play 🎮\n"
                           "    2 No Exit ❌\n"
                           "    "))
    if game_start != 1:
        break

    else:
        for a in range(1, 6):
            user_input = int(input("\n"
                                   "    Available Choice\n"
                                   "    1 Rock 👊\n"
                                   "    2 Paper 📜\n"
                                   "    3 Scissor ✌️\n"
                                   "    "))
            if user_input == 1:
                user_choice = "Rock 👊"
            elif user_input == 2:
                user_choice = "Paper 📜"
            elif user_input == 3:
                user_choice = "Scissor ✌️"

            computer_choice = random.choice(game)
            print("Your Choice =>", user_choice)
            print("Computer Choice =>", computer_choice)

            if computer_choice == user_choice:
                print("Game Draw")
                user_score = user_score + 1
                computer_score = computer_score + 1
            elif ((computer_choice == "Rock 👊" and user_choice == "Paper 📜") or
                  (user_choice == "Paper 📜" and computer_choice == "Rock 👊") or
                  (computer_choice == "Rock 👊" and user_choice == "Scissor ✌️") or
                  (user_choice == "Scissor ✌️" and computer_choice == "Rock 👊") or
                  (computer_choice == "Paper 📜" and user_choice == "Scissor ✌️") or
                  (user_choice == "Scissor ✌️" and computer_choice == "Paper 📜")):
                print("You Win 🤩")
                user_score = user_score + 1
            else:
                print("Computer win")
                computer_score = computer_score + 1
        print("\n")
        print("Your Score:", user_score)
        print("Computer Score:", computer_score)
        if computer_score == user_score:
            print("Game Draw")
        elif user_score > computer_score:
            print("\n"
                  "    Mr.", user_name, "\n"
                  "    You winner\n"
                  "    🏆🥳🤩🤓"
                  "    ")
        else:
            print("You Lose Mr.", user_name, "😭😢😞")

            # code end here!
