#write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:
sum = 0
for number in range(2 , 101, 2):
    sum += number

print(sum)