import random
min_value=1
max_value=6
roll_again="y"
while roll_again=="y" or roll_again=="yes":
    print("Rolling the dice....\n You Number is ",random.randint(min_value,max_value))
    roll_again=input("Want to roll the Dice Again(y/n)or(yes/no):")
print("The Game has ended , Thank you!")