
#yes/no checking function
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
    print("Program continue ")
    print()

#main routine
played_before=yes_no("Have you played this game before?")

if played_before == "No":
    instructions()
else:
    print("Program continues")


