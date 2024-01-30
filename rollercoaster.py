print("welcome to the rollercoaster!")
print("enter your height in cm")
height = int(input())
bill = 0;
if height >= 120:
    print("enter your age to check if you can ride the rollercoaster")
    age = int(input())
    if age <12:
        bill = 5
        print(f"Children ticket: {bill}")
    elif age<=18:
        bill = 7
        print(f"Youth ticket: {bill}")
    elif age<45 and age>55:
       bill = 12
       print(f"Adult or aged ticket: {bill}")
    elif age>=45 and age<=55:
        bill = 0
        print(f"Midlife crisis ticket: {bill}")
    else:
      bill=0
      print(f"Adult ticket: {bill}")
    print("Do you need a photo?")
    photo = input()
    if photo == "Y":
        bill +=3;
        print(f"you have to pay {bill}")
    else:
        print(f"The total bill is {bill}")
else:
    print("Sorry please grow to ride a rollecoaster")
