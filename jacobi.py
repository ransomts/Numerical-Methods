import sys
import math

'''
Implementation of the Jacobi method of determining the solutions of
a diagonally dominant system of linear equations. A matrix is diagonally
dominant if the magnitude of the diagonal element is greater than or equal 
to the sum of the magnitudes of the other elements in the row.
'''

def jacobi (A, b, tol, max_its, n, x, delta):
    for k in range(1, max_its, 1):
        norm = 0
        for i in range(0, n-1):
            if (A[i,i] < delta):
                print("Diagonal too small\n")
                sys.exit()
            xnew[i] = b[i]
            for j in range(0, i-1, 1):
                xnew[i] = xnew[i] - A[i, j] * x[j]
            for j in range(i+1, n-1, 1):
                xnew[i] = xnew[i] - A[i, j] * x[j]
            xnew[i] = xnew[i] / A[i, i]
            norm = norm + abs(xnew[i] - x[i])
        if (norm < tol):
            print(xnew)
            sys.exit()
        for i in range(0, n-1, 1):
            x[i] = xnew[i]
    print("Maximum iterations exceeded")
