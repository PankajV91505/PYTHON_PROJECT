def is_palindrome():
    text = input("Enter a word or phrase: ").replace(" ", "").lower()
    if text == text[::-1]:
        print("It's a palindrome! ✅")
    else:
        print("Not a palindrome ❌")

is_palindrome()
