

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


#main routine
show_instruction=yes_no("Have you played this game before? ")
print(f"you entered '{show_instruction}'")
print()
having_fun=yes_no("are you having fun? ")
print(f"you entered '{having_fun}'")
