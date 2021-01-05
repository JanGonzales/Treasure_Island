# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
Combined = name1 + name2
Name_lower = Combined.lower()

Var_True = Name_lower.count("t") + Name_lower.count("r") + Name_lower.count("u") + Name_lower.count("e")
Var_Love = Name_lower.count("l") + Name_lower.count("o") + Name_lower.count("v") + Name_lower.count("e")
score = int(str(Var_True) + str(Var_Love))

if score <= 10 or score >= 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")
