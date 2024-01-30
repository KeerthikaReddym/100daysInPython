print("welcome to love calculator")
name1 = input("whats your name?\n")
name2 = input("whats their name?\n")
name3 = name1 + name2
Tscore = 0
LScore = 0
name3 = name3.lower()
Tscore = name3.count("t") + name3.count("r") + name3.count("u") + name3.count(
    "e")
LScore = name3.count("l") + name3.count("o") + name3.count("v") + name3.count(
    "e")
score = str(Tscore) + str(LScore)
if (int(score) < 10 or int(score) > 90):
    print(f"your score is {score}, you go together like coke and mentos")
elif (int(score) > 40 and int(score) < 50):
    print(f"your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")
