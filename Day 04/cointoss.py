# write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random
#Write the rest of your code below this line 👇
print("Head or Tails")
toss = random.randint(0,1)
if toss == 1:
    print("Heads")
else:
    print("Tails")