# Python program to convert decimal number into binary number using recursive function
binaryform = ""
n = int(input("Enter an integer: "))# Take decimal number from user
"""Function to print binary number for the input decimal using recursion"""
while n >= 1:
   strdigit= str(n % 2)
   n= n/2
   binaryform += strdigit
binaryform = binaryform[::-1]
print(binaryform)
