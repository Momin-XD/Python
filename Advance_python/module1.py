'''
# using walrus operator         assigning while performing an action
if (n:=len([1,2,3,4,5]))>3:
    print(f"list is too long ({n} elements, expected <=3)")
'''


'''
# Type definations       used just to define type to make the code user understandable
from typing import List, Union, Tuple 

n : int = 5

name: str = "Harry"

def  sum(a: int, b: int) -> int:
    return a+b
'''



'''
# Use of match case 
def http_status(status): 
    match status:  
        case 200: 
            return "OK" 
        case 404: 
            return "Not Found" 
        case 500: 
            return "Internal Server Error" 
        case _: 
            return "Unknown status"  

print(http_status(5007))
'''


'''
#  dictionary union
dict1={'a' : 1,'b' :2}
dict2={'c' : 3,'d' :4}
merge= dict1 | dict2
print(merge)
'''


'''
#                               EXCEPTION HANDLING   

# TRY ---  EXCEPT  
try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except ValueError as v:     #here we are using except so the programm will continue afetr showing an error,that means it will not crash
    print("Heyyyy")  
    print(v)
    
except Exception as e:
    print(e) 

print("Thank You")


# TRY --- RAISE
# raising zero division error
a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if(b == 0):
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")           #here we are using raise so the programm will not continue afetr showing an error,and will crash the programm
else:
    print(f"The division a/b is {a/b}")



# TRY --- ELSE
try:
    a = int(input("Hey, Enter a number: "))
    print(a)
    
except Exception as e:
    print(e) 

else:                # it will execute only when tri is successful
    print("I am inside else")

    

# TRY --- FINALLY
def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return

        
    except Exception as e:
        print(e) 
        return


    finally:
        print("Hey I am inside of finally")


main()
'''


'''
#                  global and local variables
a = 89

def fun(): 
    # global a
    a = 3
    print(a)


fun()
print(a)
'''


'''
#                        WAYS TO MAKE THE WORD SHORTER AND EASIER

#           ENUMERATE FUNC
l = [3, 513, 53, 535]

# index = 0
# for item in l:
#     print(f"The item number at index {index} is {item}")
#     index += 1

# This can be simplified using enumerate function

for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")


#         LIST COMPREHENSIOM
myList = [1, 2, 9, 5, 3, 5]

# squaredList = []
# for item in myList:
#     squaredList.append(item*item)

squaredList = [i*i for i in myList]

print(squaredList)
'''


'''
try:
    with open("1.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("2.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("3.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)


print("Thank You!")
'''

'''
l=[i for i in  range(1,11)]
for index,item in enumerate(l):
    if index==2 or index==4 or index==6:
        print(item)
'''


'''
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))

try:
        print(a/b)

except ZeroDivisionError as e:
        print("Infinity")
        print(e)
'''