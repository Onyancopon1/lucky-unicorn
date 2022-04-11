import random

tokens =["unicorn","horse","zebra","donkey",]

#testing loop to generate 20 token
for item in range(20):
    token=random.choice(tokens)
    print(token, end='\t') #can wrap output making it easier to screenshot

