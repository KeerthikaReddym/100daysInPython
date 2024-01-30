print("Welcome to leap year claculator")
print("enter the year you want to check if its leap year or not")
year = int(input())
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("its a leap year")
        else:
            print("the entered year is not a leap year")
    else:
        print("the entered year is a leap year")

else:
    print("the entered year is not a leap year")
