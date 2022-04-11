"""LU base component
components added after they have been created and tested"""
#yes/no checking function
import random


def yes_no(question_text):
    while True:


        #asked user if they have played this before
        answer=input(question_text).lower()

        #if they say yes output 'program continue'
        if answer == "yes" or answer=='y':
            answer="Yes"
            return answer
        #if they say no output 'Display instruction'
        elif answer == "no" or answer=='n':
            answer ="No"
            return answer

        #otherwise show 'error'
        else:
            print("please enter 'yes' or 'no'")

#function to display instruction
def instructions():
    print()
    print(formatter("*","how to play"))
    print()
    print("choose a starting amount to play with - must be between $1 and $10")
    print()
    print("Then press <enter> to play. you will get a random token which might"
          "be a Horse, a Zebra, a Donkey, ora Unicorn.")
    print()
    print("it costs $1 to play each round but, depending on your prize, you"
          "\tUnicorn: $5(balance increases by $4\n"
          "\tHorse: $0.5(balance decreases by $0.5\n"
          "\tZebra: $0.5(balance decreases by $0.5\n"
          "\tDonkey: $0 (balance decreases by $1\n")
    print("\nSee if you can avoid donkeys, get the unicorns, and finish with "
          "more money than you started with.\n")
    print("*"*50)
    print()


#number checking function
def num_check(question,low,high):
    error = "that was not valid input\n"\
            "please enter a number between{} and {}\n".format(low,high)

    #keep asking until a valid amount (1-10) is entered
    while True:
        try:
            #ask for amount
            response=int(input(question))

            #checking for number within the required range
            if low<=response<=high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

#function to generate random token
def generate_token(balance):

    round_played=0
    play_again =""

    #testing loop to generate 5 tokens
    while play_again !="x":
        round_played+=1 #keep track of rounds
        print(formatter(".", f"Round {round_played}"))
        print()
        number = random.randint(1,100)


        #adjust balance
        #if the random nuber is between 1 and 5
        #user gets a Unicorn (add $4 to balance)
        if 1 <=number<=5:
            balance+=4
            print(formatter("!","congratulations you got Unicorn"))

        #if the random number is between 6 and 36
        #user gets a donkey (subtract $1 from balance)
        elif 6<=number<=36:
            balance-=1
            print(formatter("D","unlucky you got Donkey"))
        #in all the other case the token must be a horse or a zebra
        #(subtract $0.50 from the balance in either case)
        else:
            #if the number is even, set the token to zebra
            if number %2==0:
                balance -=0.5
                print(formatter("Z","You got Zebra"))
            #otherwise , set the token to horse
            else:
                balance-= .5
                print(formatter("H","You got Horse"))
                print()

        #output
        print(f"Your balance is now:${balance:.2f}")
        if balance < 1:
            print("\nSorry but you have run out of money")
            play_again="x"
        else:
            play_again=input("\nDo you want to play another round?""\n<enter>"
                             "again or 'X' to exit ").lower()
        print()
    return balance


#function to format text output
def formatter(symbol,text):
    sides=symbol *3
    formatted_text=f"{sides}{text}{sides}"
    top_bottom=symbol* len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"

#main routine  go here
print(formatter("-", "Welcome to the Lucky Unicorn Game"))
print()

played_before=yes_no("Have you played this game before?")

if played_before == "No":
    instructions()


#ask user how much they want to play with
starting_balance=num_check("How much would you like to play with?$", 1,10)
print(f"You are playing with ${starting_balance:.2f}")

closing_balance =generate_token(starting_balance)
print("Thanks for playing ")
print(f"you started with ${starting_balance:.2f}")
print(f"and leave with ${closing_balance:.2f}")
print()
print(formatter("*","Goodbye"))



