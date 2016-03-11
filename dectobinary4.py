# Python program to convert decimal number into binary number using recursive function
def binary(n, binaryform = 0,i=1):
   """Function to print binary number for the input decimal using recursion"""
   if n >= 1:
	digit= n % 2
	binaryform += digit*i
	i*=10
	binary(n/2, binaryform, i)
   else:
	print(binaryform)
dec = int(input("Enter an integer: "))# Take decimal number from user
binary(dec)




###//////////////////////////////////////////////////////////////////
# the other form
# Python program to convert decimal number into binary number using recursive function
def binary(n, binaryform,i):
   """Function to print binary number for the input decimal using recursion"""
   if n < 1:
        return binaryform
   else:
	digit= n % 2
	binaryform += digit*i
	#print(binaryform)
	i*=10
	print(binaryform)
	return binary(n/2, binaryform, i)

dec = int(input("Enter an integer: "))# Take decimal number from user
aa = binary(dec, 0, 1)
print(aa)
