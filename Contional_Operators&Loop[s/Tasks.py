# Task_1

num=int(input("Enter a number: "))
if num % 2 ==0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")


# Task_2
sum = 0
for i in range(1, 51):
    sum += i
print("Sum of numbers from 1 to 50 is:", sum)