# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
#bmi = weight (kg) /height (m2) * height

bmi  = float(weight) / float(height) ** 2
print(round(bmi))
