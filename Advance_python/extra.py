#           LMADA FUNCTION

# def square(n):
#     return n*n 

square = lambda x: x*x

print(square(5))


#            JOIN FUNC
a = ["Harry", "Rohan", "Shubham"]

final = "::".join(a)
print(final)


'''
#           FORMAT FUNC
a = "{1} is a good {0}".format("harry", "boy")

print(a)

# 
name = input("Enater Name: ")
marks = int(input("Enater Marks: "))
phone = int(input("Enater Phone Number: "))

s = "The name of the student is {}, his marks are {} and phone number is {}".format(name, marks, phone)

print(s)
'''


# l=[str(7*i) for i in range(1,11)]

# s="\n".join(l)
# print(s)



# l=[i for i in range(1,101)]
# def div(a):
#     if a%5==0:
#         return True
#     return False
# s=filter(div,l)
# print(list(s))





# from functools import reduce
# l=[324,4523,134,3248,2731]

# def gr(a,b):
#     if a>b:
#         return a
#     return b

# print(reduce(gr,l))