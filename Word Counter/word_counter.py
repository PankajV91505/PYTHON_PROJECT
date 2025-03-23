def word_counter():
    text = input("Enter a sentence or paragraph: ")
    
    word_count = len(text.split())  # Count words
    char_count = len(text)  # Count characters
    
    print(f"\nWord Count: {word_count}")
    print(f"Character Count (including spaces): {char_count}")

if __name__ == "__main__":
    word_counter()
