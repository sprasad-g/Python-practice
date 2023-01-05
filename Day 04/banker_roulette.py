# write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
# not allowed to use the choice() function.
# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
index  = random.randint(0, len(names)-1)
print(names[index])

person = random.choice(names)
print(person)