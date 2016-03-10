# Python program to convert decimal number into binary number using recursive function
def binary(n):
   global binaryform
   binaryform = ""
   """Function to print binary number for the input decimal using recursion"""
   if n >= 1:
	strdigit= str(n % 2)
	binary(n/2)
	binaryform += strdigit
dec = int(input("Enter an integer: "))# Take decimal number from user
binary(dec)
print(binaryform)


