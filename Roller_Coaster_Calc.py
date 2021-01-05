Height = float(input("Please Enter your Height: "))
Age = int(input("Please Enter your age: "))
Bill = 0

if Height > 120:
    if 45 <= Age or Age >= 55:
        print("You ride for free, pizza's on me")
    elif Age <= 12:
        Bill += 5
    else:
        Bill += 12
else:
    print("leider! you are not tall enough :(")

Photos = input("Do you want your photo taken? y/N").lower()
if Photos == "y":
    Bill += 3

print(f"Your total bill is £{Bill}")