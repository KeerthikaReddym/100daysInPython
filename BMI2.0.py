print("welcome to BMI Calculator")
print("enter your height in meters")
height = float(input())
print("enter your weight in kgs")
data = float(input())
sq = height*height
print(sq)
bmi = data/sq
print("your BMI is",bmi)
if bmi<18.5:print(f"your BMI is {bmi}, you are underweight")
elif bmi<25:print(f"your BMI is {bmi}, you are normal")
elif bmi<30:print(f"your BMI is {bmi}, you are overweight")
elif bmi<35 and bmi<34.9:print(f"your BMI is {bmi}, you are obese")
else:
  print(f"your BMI is {bmi}, you are clinically obese")


