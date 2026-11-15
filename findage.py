Birthyear=int(input("Enter your birth year:"))
currentyear=int(input("Enter current year:"))
if Birthyear==1998:
    if currentyear==2026:
        age=currentyear-Birthyear
        print("your age is ",age)
else:
    print("network error")