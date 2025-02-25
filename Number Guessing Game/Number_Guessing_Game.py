import random

def play_game():
    print("🎯 Welcome to the Number Guessing Game!")
    number_to_guess = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("⚠️ Please enter a number between 1 and 100.")
            elif guess < number_to_guess:
                print("🔼 Too low! Try again.")
            elif guess > number_to_guess:
                print("🔽 Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("❌ Invalid input! Please enter a number.")

if __name__ == "__main__":
    play_game()
