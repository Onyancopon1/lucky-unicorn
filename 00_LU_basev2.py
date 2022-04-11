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
    print("**** How to play ****")
    print()
    print("The rules of the game will go here")
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
        number = random.randint(1,100)

        #adjust balance
        #if the random nuber is between 1 and 5
        #user gets a unicorn (add $4 to balance)
        if 1 <=number<=5:
            token="unicorn"
            balance+=4

        #if the random number is between 6 and 36
        #user gets a donkey (subtract $1 from balance)
        elif 6<=number<=36:
            token="donkey"
            balance-=1

        #in all the other case the token must be a horse or a zebra
        #(subtract $0.50 from the balance in either case)
        else:
            #if the number is even, set the token to zebra
            if number %2==0:
                token="zebra"
                balance -=0.5

            #otherwise , set the token to horse
            else:
                token="horse"
                balance-= .5

        #output
        print(f"Round{round_played}. Token: {token}, Balance:${balance:.2f}")
        if balance < 1:
            print("\nSorry but you have run out of money")
            play_again="x"
        else:
            play_again=input("\nDo you want to play another round?""\n<enter> to play
                            again or 'X' to exit ").lower()
            print()
        return balance


#function to format text output
def formatter(symbol,text):
    sides=symbol *3
    formatted_text=f"{sides}{text}{sides}"
    top_bottom=symbol* len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"

#main routine  go here
print(formatter("-", "welcome to the lucky Unicorn game"))
print()

played_before=yes_no("Have you played this game before?")

if played_before == "No":
    instructions()


#ask user how much they want to play with
starting_balance=num_check("Hoe much would you like to play with?$", 1,10)
print(f"You are playing with ${starting_balance:.2f}")

closing_balance =generate_token(starting_balance)
print("Thanks for playing ")
print(f"you started with ${starting_balance:.2f}")
print(f"and leave with ${closing_balance:.2f}")
print()
print(formatter("*","Goodbye"))



