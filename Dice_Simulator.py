import random
def roll():

    op=random.randint(1,6)
    return op


while(True):
    print ("You rolled ",roll())
    choice=input("Wanted to play again (Yes/No) ")
    if choice!="Yes":
        break
print("Thank you :)")