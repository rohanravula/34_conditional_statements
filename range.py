# a=range(5) #(0,5) range
# print(a,type(a))

# a=range(9)
# for n in a:
#     print(n) #the output will be in vertically but it starts form 0 to 8
"OR"
# for n in range(7):
#     print(n) #the output will be in vertically but it starts form 0 to 6. the above print statemt and this statement both are same this is the second method

"TO GET IN HORIZONTAL"
# for b in range(4):
#     print(b,end=" ") # the output will be in horozontal starts form 0 to 3 with space

"IF WE WANT TO START FORM THE CERTAIN NUMBER WE NEED TO DO LIKE THIS"
# for n in range(3,9):
#     print(n) # the  output will be the number starts form 3 to 8 in verticall 

"print odd numbers"
# for n in range(1,9,2):
#     print(n) #1 3 5 7 , the numbers will be skkiped by 2

"print even numbers"
# for n in range (0,15,2):
#     print(n) #0 2 4 6 8 10 12 14 this are printing even numbers

"in horozontal manner"
# a=1,2,3,4,5
# print(*a) # 1 2 3 4 5

# a=range(10)
# print(a) #(0,10)

"how to enter the range number though using the input method"
# n=int(input("Enter the value of n:"))
# for i in range(1,n+1):
#     print(i,end="\n") 

"how to enter the values in reverse order"
# for n in range(10,0,-1):
#     print(n) # the output will start form the 9 to 1 in reverse order.

"in reverse order but at last we need zero so we need to do like this"
# for i in range(10,-1,-1):
#     print(i)

"if we have multile print statements"
# n=int(input("Enter any integer number:"))
# for i in range (n):
#     print(i)
#     print(i)
#     print(i)
#     print(i) #the out put will be 4 times 0 and 4 times 1 if we pass the value as 2

"when the print statement belong to for loop"
# n=int(input("enter number"))
# for i in range (n):
#     print(i)
#     print(i)
#     print(i)
#     print("the loop has been came")


"when the print statement is not belong to for loop "
# n=int(input("number"))
# for i in range (n) :
#     print(i)
#     print(i)
#     print(i)
#     print("the loop has came")
# print("done")

# c=int(input("any number"))
# for c in range (25,c):
#     print(c) #the ouptput will be blank coz we cant go back in the numbers.

