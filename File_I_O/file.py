# f = open("file.txt")
# data=f.read()
# print(data)
# f.close()


# f=open('file.txt')
# lines = f.readlines()  #IT READS LINE BY LINE
# print(lines)
# f.close()


# f=open('file.txt')
# line1 = f.readline()  #IT READS LINE BY LINE
# line2 = f.readline()  #IT READS LINE BY LINE
# line3 = f.readline()  #IT READS LINE BY LINE
# line4 = f.readline()  #IT READS LINE BY LINE
# print(line1)
# print(line2)
# print(line3)
# print(line4)
# f.close()



# # 
# f=open('file.txt')
# line=f.readline()
# while (line !=""):
#     print(line)
#     line=f.readline()
# f.close()


# USING WITH STATEMENT
# with open('file.txt') as f:
#     print(f.read())



#  Checking the word present or not
# f=open("poems.txt",'r')
# lines=f.read()
# print("twinkle" in lines)
# f.close()



# Writing Tables 
# for i in range(2,21):
#     with open(f"C:\\Python\\File_I_O\\Tables\\TableOf_{i}","a") as f:
#             for x in range(1,11):
#                 f.write(f'{i} X {x} = {i*x}\n')


# Replacing a word from file
# with open("file.txt") as f :
#     word=f.read()
# list=['Donkey','lul','bure','gadhe']
# for l in list:
#     word=word.replace(l,len(l)*"#")
# with open("file.txt","w") as f :
#     f.write(word)


# We can open multiple files in a single func
with (
    open('file.txt') as f1,
    open('Myfile.txt') as f2
):
    print(f1.read())
    print("\n")
    print(f2.read())

