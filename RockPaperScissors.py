import random
list1 = ["r","p","s"]

emojis= {
    "r": "🧱",
    "p": "📜",
    "s": "✂"
}

def get_user_choice():
    choice = input("rock, paper or scissors? (r,p,s):").lower()
    if choice in list1:
        return choice
    else:
        print("INVALID CHOICE")


def display_choices(choice,computer_choice):
    print("you chose",emojis.get(choice))
    print(f"computer chose {emojis.get(computer_choice)}")


def determine_winner(choice,computer_choice):
    if choice == computer_choice:
        print("tie")
    elif (choice == "r" and computer_choice == "s") or (choice == "s" and computer_choice == "p") or ( choice == "p" and computer_choice == "r"):
        print("you won!")
    else:
        print("you lose")


def game_play():
    while True:
        choice = get_user_choice()
        computer_choice = random.choice(list1)
        display_choices(choice,computer_choice)
        determine_winner(choice,computer_choice)

        should_continue = input("continue ? yes or no:").lower()
        if should_continue == "no":
            print("Thanks for playing")
            break

game_play()





