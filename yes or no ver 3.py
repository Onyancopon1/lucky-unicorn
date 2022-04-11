

instruction=""
while instruction != "x":

    #asked user if they have played this before
    instruction=input("have you play this game before?: ").lower()
    #if they say yes output 'program continue'
    if instruction == "yes" or instruction=='y':
        print("program continue ")

    #if they say no output 'Display instruction'
    elif instruction == "no" or instruction=='n':
        print("Display instruction")

    #otherwise show 'error'
    else:
        print("please enter 'yes' or 'no'")

    print(f"you entered '{instruction}'")
