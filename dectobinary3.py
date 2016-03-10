# Python program to convert decimal number into binary number using nonrecursive function way2
n = int(input("Enter an integer: "))# Take decimal number from user
binaryform=0
i=1
"""Function to print binary number for the input decimal using recursion"""
while n >= 1:
	digit= n % 2
	binaryform += digit*i
        i*=10
	n = n/2

print(binaryform)
