import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 4:
                print("Password should be at least 4 characters long.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    password = generate_password(length)
    print(f"\nYour generated password: {password}")

if __name__ == "__main__":
    main()
