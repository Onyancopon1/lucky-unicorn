

user_balance=int(input("How much do you want to play with (must be an"
                       "integer between 1 and 10) $"))

#keep asking until a valid amount (1-10) is entered
while not 1<=user_balance<= 10:
    print("Try again. PLease enter a whole number between 1 and 10")
    #ask for the input
    user_balance=int(input("How much do you want to play with $"))

print(f"You are  playing with ${user_balance}")



