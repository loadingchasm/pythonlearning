# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lower = name1.lower()
name2_lower = name2.lower()

combinedName = name1_lower + name2_lower

trueTotalCount = combinedName.count("t") + combinedName.count("r") + combinedName.count("u") + combinedName.count("e")

loveTotalCount = combinedName.count("l") + combinedName.count("o") + combinedName.count("v") + combinedName.count("e")

loveScore = int(str(trueTotalCount) + str(loveTotalCount))

if loveScore < 10 or loveScore > 90:
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif loveScore >= 40 and loveScore <=50:
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}.")
