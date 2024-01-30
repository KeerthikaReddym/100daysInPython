print("welcome to BMI Calculator")
print("enter your height in meters")
height = float(input())
print("enter your weight in kgs")
data = float(input())
sq = height*height
print(sq)
bmi = data/sq
print("your BMI is",bmi)
if bmi<18.5:print("your are underweight")
if bmi>18.5 and bmi<24.9:print("your are normal")
if bmi>25 and bmi<29.9:print("your are overweight")
if bmi>30 and bmi<34.9:print("your are obese")

