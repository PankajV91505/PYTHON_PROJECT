email = input("Enter your email: ")
k,j,d=0,0,0
if len(email) >=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="@" or i=="." or i=="_":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("Email is invalid")
            else:
                print("Email must have .com or .in at the end")
            
        else:
            print("Email must have one @ symbol")
    else:
        print("Email must start with a letter")
else:
    print("Email is too short")