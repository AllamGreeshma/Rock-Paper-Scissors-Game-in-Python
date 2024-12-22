import random

def get_user_choice():
    print("Choose one of the following:")
    print("1. 🪨 Stone")
    print("2. 📄 Paper")
    print("3. ✂️ Scissors")
    choice = int(input("Enter your choice (1-3): "))
    if choice < 1 or choice > 3:
        print("Invalid choice! Please choose again.")
        return get_user_choice()
    return choice

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    choices = ["🪨", "📄", "✂️"]
    print(f"\nYou chose: {choices[user_choice - 1]}")
    print(f"Computer chose: {choices[computer_choice - 1]}")
    
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to 🪨 Stone 📄 Paper ✂️ Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_game()
