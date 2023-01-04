# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word 
# TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
 
both_name = (name1 + name2).lower()

T =  both_name.count("t")
R =  both_name.count("r")
U =  both_name.count("u")
E =  both_name.count("e")
true = T+R+U+E
L =  both_name.count("l")
O =  both_name.count("o")
V =  both_name.count("v")
E =  both_name.count("e")
love = L+O+V+E

score = int(str(true) + str(love))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >=40) and (score =< 50):
        print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}. ")


