import random

def play_game():
    print("\nWelcome to the Number Guessing Game")
    print("Choose your difficulty level:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-500, 5 attempts)")

    # Difficulty selection
    choice = input("Enter 1, 2, or 3: ")
    
    if choice == "1":
        secret_number = random.randint(1, 50)
        attempts_allowed = 10
        range_text = "1 to 50"
    elif choice == "2":
        secret_number = random.randint(1, 100)
        attempts_allowed = 7
        range_text = "1 to 100"
    elif choice == "3":
        secret_number = random.randint(1, 500)
        attempts_allowed = 5
        range_text = "1 to 500"
    else:
        print("Invalid choice! Defaulting to Medium.")
        secret_number = random.randint(1, 100)
        attempts_allowed = 7
        range_text = "1 to 100"

    print(f"\nI have chosen a number between {range_text}. You have {attempts_allowed} attempts!")

    # Game loop
    attempts = 0
    score = 100
    while attempts < attempts_allowed:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("⚠️ Please enter a valid number!")
            continue

        attempts += 1
        difference = abs(secret_number - guess)

        if guess == secret_number:
            print(f"🎉 Correct! The number was {secret_number}.")
            print(f"You guessed it in {attempts} attempts with a score of {score} 🏆")
            break
        elif difference <= 5:
            print("Very close!")
            score -= 5
        elif difference <= 10:
            print("Almost close!")
            score -= 10
        elif guess < secret_number:
            print("Too low!")
            score -= 15
        else:
            print("Too high!")
            score -= 15

        print(f"Current Score: {score}")
        print("___________________________")
    else:
        print(f"Out of attempts! The number was {secret_number}.")
        print("Final Score: 0")

# Main loop (Replay option)
while True:
    play_game()
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break
