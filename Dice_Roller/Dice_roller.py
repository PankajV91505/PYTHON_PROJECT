import random

def roll_dice():
    return random.randint(1, 6)

def play_dice_roller():
    while True:
        input("Press Enter to roll the dice... (or type 'exit' to quit) ")
        dice_value = roll_dice()
        print(f"You rolled a {dice_value} 🎲")
        
        play_again = input("Roll again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! 🎲")
            break

if __name__ == "__main__":
    play_dice_roller()
