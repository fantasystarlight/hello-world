# hello-world
just another respository

import numpy

A=[[9,3,7],[6,5,2],[8,4,1]]
B=[[1,2,3],[4,5,6],[7,8,9]]
import copy
def entropy(X):
    c=[]
    for i in range(len(X)):
        for j in range(len(X[0])):
            c.append((X[i][j]-B[i][j])**2)
    C = sum(c)
    return C

def transfer(X):
    x = []
    for i in range(12):
        X = copy.deepcopy(X)
        x.append(X)
    
        
    x[0][0][0], x[0][0][1] = x[0][0][1], x[0][0][0]
    x[1][0][1], x[1][0][2] = x[1][0][2], x[1][0][1]
    x[2][1][0], x[2][1][1] = x[2][1][1], x[2][1][0]
    x[3][1][1], x[3][1][2] = x[3][1][2], x[3][1][1]
    x[4][2][0], x[4][2][1] = x[4][2][1], x[4][2][0]
    x[5][2][1], x[5][2][2] = x[5][2][2], x[5][2][1]
    x[6][0][0], x[6][1][0] = x[6][1][0], x[6][0][0]
    x[7][1][0], x[7][2][0] = x[7][2][0], x[7][1][0]
    x[8][0][1], x[8][1][1] = x[8][1][1], x[8][0][1]
    x[9][1][1], x[9][2][1] = x[9][2][1], x[9][1][1]
    x[10][0][2], x[10][1][2] = x[10][1][2], x[10][0][2]
    x[11][1][2], x[11][2][2] = x[11][2][2], x[11][1][2]

    y = 1000000
    for k in range(len(x)):
        c = entropy(x[k])
        
        if y > c:
            y = c
            n = k
    print(y,n)
    return([n], x[n])

def iterat(X):
    while entropy(X) != 0:
        X = transfer(X)[1]
        Y = numpy.array(X)
        print(Y)
    return (X)

iterat(A)
