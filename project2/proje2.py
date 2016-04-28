# -*- coding: utf-8 -*-
import random 
import numpy as np
import timeit
from timeit import Timer
from optparse import OptionParser
from math import ceil, log
n=2
########################################Brute Force Matrix Multiplication#######################################################################################
def BFMultiplication(A,B,n):
##CarpimBfm is the result of Brute Force Matrix Multiplication of two matrix
	CarpimBfm = np.empty([n, n], dtype = int)
	for i in range(n):
		for j in range(n):
			CarpimBfm[i][j]=random.randint(0,9)
	for i in range(n):
		for j in range(n):
			q=0
			for k in range(n):
				q = q + A[i][k]*B[k][j]
				CarpimBfm[i][j]=q
	#print("BruteForce", CarpimBfm)
	return(CarpimBfm)
#######################################End of Brute Force Multiplication#########################################################################################



########################################Strassen Matrix Multiplication###########################################################################################
##CarpimStrassen is the result of the Strassen Matrix Multiplication of two matrix
def add(A, B):
    n = len(A)
    C = [[0 for j in xrange(0, n)] for i in xrange(0, n)]
    for i in xrange(0, n):
        for j in xrange(0, n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def subtract(A, B):
    n = len(A)
    C = [[0 for j in xrange(0, n)] for i in xrange(0, n)]
    for i in xrange(0, n):
        for j in xrange(0, n):
            C[i][j] = A[i][j] - B[i][j]
    return C

def strassenR(A, B):
    """ Implementation of the strassen algorithm, similar to 
        http://en.wikipedia.org/w/index.php?title=Strassen_algorithm&oldid=498910018#Source_code_of_the_Strassen_algorithm_in_C_language
    """
    n = len(A)

    # Trivial Case: 1x1 Matrices
    if n == 1:
        return [[A[0][0]*B[0][0]]]
    else:
        # initializing the new sub-matrices
        newSize = n/2
        a11 = [[0 for j in xrange(0, newSize)] for i in xrange(0, newSize)]
        a12 = [[0 for j in xrange(0, newSize)] for i in xrange(0, newSize)]
        a21 = [[0 for j in xrange(0, newSize)] for i in xrange(0, newSize)]
        a22 = [[0 for j in xrange(0, newSize)] for i in xrange(0, newSize)]

        b11 = [[0 for j in xrange(0, newSize)] for i in xrange(0, newSize)]
        b12 = [[0 for j in xrange(0, newSize)] for i in xrange(0, newSize)]
        b21 = [[0 for j in xrange(0, newSize)] for i in xrange(0, newSize)]
        b22 = [[0 for j in xrange(0, newSize)] for i in xrange(0, newSize)]

        aResult = [[0 for j in xrange(0, newSize)] for i in xrange(0, newSize)]
        bResult = [[0 for j in xrange(0, newSize)] for i in xrange(0, newSize)]

        # dividing the matrices in 4 sub-matrices:
        for i in xrange(0, newSize):
            for j in xrange(0, newSize):
                a11[i][j] = A[i][j];            # top left
                a12[i][j] = A[i][j + newSize];    # top right
                a21[i][j] = A[i + newSize][j];    # bottom left
                a22[i][j] = A[i + newSize][j + newSize]; # bottom right

                b11[i][j] = B[i][j];            # top left
                b12[i][j] = B[i][j + newSize];    # top right
                b21[i][j] = B[i + newSize][j];    # bottom left
                b22[i][j] = B[i + newSize][j + newSize]; # bottom right

        # Calculating p1 to p7:
        aResult = add(a11, a22)
        bResult = add(b11, b22)
        p1 = strassen(aResult, bResult) # p1 = (a11+a22) * (b11+b22)

        aResult = add(a21, a22)      # a21 + a22
        p2 = strassen(aResult, b11)  # p2 = (a21+a22) * (b11)

        bResult = subtract(b12, b22) # b12 - b22
        p3 = strassen(a11, bResult)  # p3 = (a11) * (b12 - b22)

        bResult = subtract(b21, b11) # b21 - b11
        p4 =strassen(a22, bResult)   # p4 = (a22) * (b21 - b11)

        aResult = add(a11, a12)      # a11 + a12
        p5 = strassen(aResult, b22)  # p5 = (a11+a12) * (b22)   

        aResult = subtract(a21, a11) # a21 - a11
        bResult = add(b11, b12)      # b11 + b12
        p6 = strassen(aResult, bResult) # p6 = (a21-a11) * (b11+b12)

        aResult = subtract(a12, a22) # a12 - a22
        bResult = add(b21, b22)      # b21 + b22
        p7 = strassen(aResult, bResult) # p7 = (a12-a22) * (b21+b22)

        # calculating c21, c21, c11 e c22:
        c12 = add(p3, p5) # c12 = p3 + p5
        c21 = add(p2, p4)  # c21 = p2 + p4

        aResult = add(p1, p4) # p1 + p4
        bResult = add(aResult, p7) # p1 + p4 + p7
        c11 = subtract(bResult, p5) # c11 = p1 + p4 - p5 + p7

        aResult = add(p1, p3) # p1 + p3
        bResult = add(aResult, p6) # p1 + p3 + p6
        c22 = subtract(bResult, p2) # c22 = p1 + p3 - p2 + p6

        # Grouping the results obtained in a single matrix:
        C = [[0 for j in xrange(0, n)] for i in xrange(0, n)]
        for i in xrange(0, newSize):
            for j in xrange(0, newSize):
                C[i][j] = c11[i][j]
                C[i][j + newSize] = c12[i][j]
                C[i + newSize][j] = c21[i][j]
                C[i + newSize][j + newSize] = c22[i][j]
        return C
	

def strassen(A, B):
    assert type(A) == list and type(B) == list
    assert len(A) == len(A[0]) == len(B) == len(B[0])

    nextPowerOfTwo = lambda n: 2**int(ceil(log(n,2)))
    n = len(A)
    m = nextPowerOfTwo(n)
    APrep = [[0 for i in xrange(m)] for j in xrange(m)]
    BPrep = [[0 for i in xrange(m)] for j in xrange(m)]
    for i in xrange(n):
        for j in xrange(n):
            APrep[i][j] = A[i][j]
            BPrep[i][j] = B[i][j]
    CPrep = strassenR(APrep, BPrep)
    C = [[0 for i in xrange(n)] for j in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            C[i][j] = CPrep[i][j]
     #print C
    return C
	



########################################End of Strassen Matrix Multiplication####################################################################################


while(n<4000):
	Matrix = np.empty([n, n], dtype = int)
	#Matrix = np.empty([n, n])		
	for i in range(n):
		for j in range(n):
			Matrix[i][j]=random.randint(0,9)
	#for item in Matrix:
		#print(item)
	Matrix2=np.random.randint(0,9, size=(n, n))
	#for item in Matrix2:
		#print(item)	
	t1 = Timer(lambda: BFMultiplication(Matrix,Matrix2,n))
	print('Brute force time', t1.timeit(number=1))
	#res = strassenR(Matrix,Matrix2)
	#print("Strassen", res)
	t2 = Timer(lambda: strassenR(Matrix,Matrix2))
	print('Strassen time', t2.timeit(number=1))


	n=n*2


