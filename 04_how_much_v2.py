

error="Please enter whole number between 1 and 10\n"
valid = False


while not valid:
    try:

        user_balance=int(input("How much do you wasnt to play with? $"))


        if 0 < user_balance <=10:
            print(f"You are playing with ${user_balance}")
            valid=True
        else:
            print(error)

    except ValueError:
        print(error)




