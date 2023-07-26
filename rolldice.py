import random
min_value=1
max_value=6
roll_again="y"
while roll_again=="y" or roll_again=="yes":
    r1=random.randint(min_value,max_value)
    r2=random.randint(min_value,max_value)
    print("Rolling the dice....\n You Numbers are ",r1,r2)
    if r1==r2:
        print("Hurray! You WON")
    roll_again=input("Want to roll the Dice Again(y/n)or(yes/no):")
print("The Game has ended , Thank you!")
