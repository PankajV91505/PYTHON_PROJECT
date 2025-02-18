# condition for email validation using regex
# a-z 
# 0-9
# . , _ , @    use at one time
# .com , .in  use at {2,3} position

# more knowledge about regex use this link: https://www.w3schools.com/python/python_regex.asp

import re

email_condition ="^[a-z] + [\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

user_email = input("Enter your email: ")

if re.search(email_condition, user_email):
    print("Email is valid")
    
else:
    print("Email is invalid")

