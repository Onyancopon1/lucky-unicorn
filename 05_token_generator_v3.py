import random

tokens =["unicorn",
         "horse","horse","horse",
         "zebra","zebra","zebra",
         "donkey","donkey","donkey"]

STARTING_BALANCE=100
balance=STARTING_BALANCE

#testing loop to generate 20 tokens
for item in range(500):
    token=random.choice(tokens)


    #adjust balance
    if token=="unicorn":
        balance+=4
    elif token=="donkey":
        balance-=1
    else:
        balance-= .50

#output
print(f"Starting balance = ${STARTING_BALANCE:.2f}")
print(f"final balance =${balance:.2f}")
    


