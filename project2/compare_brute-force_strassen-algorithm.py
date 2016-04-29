# -*- coding: utf-8 -*-
from optparse import OptionParser
from math import ceil, log
import random 
import numpy as np
import timeit
from timeit import Timer
n=2

def BruteForce(A,B,n):
##CarpimBfm is the result of Brute Force Matrix Multiplication of two matrix
	CarpimBfm=np.random.randint(1,9, size=(n, n))
	for i in range(n):
		for j in range(n):
			CarpimBfm[i][j]=0
			for k in range(n):
				CarpimBfm[i][j] = CarpimBfm[i][j] + A[i][k]*B[k][j]
	#print("BruteForce", CarpimBfm)
	return(CarpimBfm)

def add_m(A, B):
    n = len(A)
    C = [[0 for j in xrange(0, n)] for i in xrange(0, n)]
    for i in xrange(0, n):
        for j in xrange(0, n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def sub_m(A, B):
    n = len(A)
    C = [[0 for j in xrange(0, n)] for i in xrange(0, n)]
    for i in xrange(0, n):
        for j in xrange(0, n):
            C[i][j] = A[i][j] - B[i][j]
    return C


def strassen(A, B, q):
    # base case: 1x1 matrix
    if q == 1:
        d = [[0]]
        d[0][0] = A[0][0] * B[0][0]
        return d
    else:
 	ns = q/2
	
        a11 = np.empty([ns, ns], dtype = int)
        a12 = np.empty([ns, ns], dtype = int)
        a21 = np.empty([ns, ns], dtype = int)
        a22 = np.empty([ns, ns], dtype = int)

        b11 = np.empty([ns, ns], dtype = int)
        b12 = np.empty([ns, ns], dtype = int)
        b21 = np.empty([ns, ns], dtype = int)
        b22 = np.empty([ns, ns], dtype = int)

        aResult = np.empty([ns, ns], dtype = int)
        bResult = np.empty([ns, ns], dtype = int)
        # dividing the matrices in 4 sub-matrices:
        for i in xrange(0, ns):
            for j in xrange(0, ns):
                a11[i][j] = A[i][j]            # top left
                a12[i][j] = A[i][j + ns]    # top right
                a21[i][j] = A[i + ns][j]    # bottom left
                a22[i][j] = A[i + ns][j + ns] # bottom right

                b11[i][j] = B[i][j]            # top left
                b12[i][j] = B[i][j + ns]    # top right
                b21[i][j] = B[i + ns][j]    # bottom left
                b22[i][j] = B[i + ns][j + ns] # bottom right
        
	p1 = strassen(add_m(a11,a22), add_m(b11,b22), ns) # p1 = (a11+a22) * (b11+b22)
        p2 = strassen(add_m(a21,a22), b11, ns) # p2 = (a21+a22) * b11
        p3 = strassen(a11, sub_m(b12,b22), ns)        # p3 = a11 * (b12-b22)
        p4 = strassen(a22, sub_m(b21,b11), ns)        # p4 = a22 * (b12-b11)
        p5 = strassen(add_m(a11,a12), b22, ns)        # p5 = (a11+a12) * b22
        p6 = strassen(sub_m(a21,a11), add_m(b11,b12), ns)        # p6 = (a21-a11) * (b11+b12)
        p7 = strassen(sub_m(a12,a22), add_m(b21,b22), ns)        # p7 = (a12-a22) * (b21+b22)
        c11 = add_m(sub_m(add_m(p1, p4), p5), p7)         # c11 = p1 + p4 - p5 + p7
        c12 = add_m(p3, p5)        # c12 = p3 + p5
        c21 = add_m(p2, p4)        # c21 = p2 + p4
        c22 = add_m(sub_m(add_m(p1, p3), p2), p6)        # c22 = p1 + p3 - p2 + p6

        # Grouping the results obtained in a single matrix:
        C = [[0 for j in xrange(0, q)] for i in xrange(0, q)]
        for i in xrange(0, ns):
            for j in xrange(0, ns):
                C[i][j] = c11[i][j]
                C[i][j + ns] = c12[i][j]
                C[i + ns][j] = c21[i][j]
                C[i + ns][j + ns] = c22[i][j]
        return C

while(n<4000):
	Matrix=np.random.randint(1,9, size=(n, n))
	Matrix2=np.random.randint(1,9, size=(n, n))
	#for item in Matrix:
	#	print(item)
	print(n,'x',n, 'Matrix')
	t2 = Timer(lambda: strassen(Matrix,Matrix2,n))
	print('Strassen time', t2.timeit(number=1))	
	t1 = Timer(lambda: BruteForce(Matrix,Matrix2,n))
	print('Brute force time', t1.timeit(number=1))

	n=n*2
