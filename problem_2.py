"""
2. Write an if statement to determine whether a variable holding a year
is a leap year.
"""
year = int(input("enter any year you want."))
if (year%4==0):
    if(year%100==0):
        if(year%400==0):
            print(f"{year} is leap year")
        else:
            print(f"{year} is not leap year")
    else:
        print(f"{year} is leap year")

else:
    print(f"{year} is not leap year")