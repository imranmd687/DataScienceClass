import numpy as np
import scipy.linalg as la

def isstablesystem(input):
    coeffArray = []
    powerArray = []

    print(input)
    data = input.split("=")
    #print(data)

    lhs = data[0].split(" + ")
    rhs = data[1].split(" + ")
    #print(lhs)
    #print(rhs)
    for lhsvar in lhs:
        lhsCoef = lhsvar.split("F")
        #print(lhsCoef)
        if lhsCoef[0] != '':
            coeffArray.append(lhsCoef[0].strip())
        else:
            coeffArray.append('0')
        powerArray.append(lhsCoef[1].strip().split("+")[1].split(")")[0])
    for rhsvar in rhs:
        rhsCoef = rhsvar.split("F")
        #print(rhsCoef)
        if rhsCoef[0] != '':
            coeffArray.append(rhsCoef[0].strip())
        else:
            coeffArray.append('0')
        if(rhsCoef[1] != '(K)'):
            powerArray.append(rhsCoef[1].strip().split("+")[1].split(")")[0])
        else:
            powerArray.append('0')

    #print(coeffArray)
    #print(powerArray)
    coeffArray = [int(i) for i in coeffArray]
    powerArray = [int(i) for i in powerArray]
    coeffArray = [x for _,x in sorted(zip(powerArray,coeffArray))]
    #print(coeffArray)
    #print(powerArray)
    highestCoeff = coeffArray[0]
    newList = [x / highestCoeff for x in coeffArray[1:]]
    lastrow = np.array(newList)
    #print(lastrow)
    # F(K+1)   [ 0 1 0 ]      F(k)
    # F(K+2) = [0 0 1]        F(k+1)
    # F(K+3)   [4/4 3/4 2/4]   F(K+2)

    #print(len(powerArray))
    b = np.identity(len(powerArray)-1)
    b = np.roll(b,1 )
    b[0][0]= 0

    #print(b[lastrow.size-1:])
    #print(lastrow)
    b[lastrow.size-1:]= lastrow[:]
    print("Matrix")
    print(b)

    eigvals, eigvecs = la.eig(b)
    eigvals = eigvals.real
    print("eigvals")
    print(eigvals)
    for x in eigvals:
        if x > 1 or x < -1:
            return False
    else:
        return True

if __name__ == "__main__":
    if isstablesystem("F(K+4) = 2F(K+3) + 4F(K+1) + 3F(K+2) + 6F(K)") == True:
        print("Stable")
    else:
        print("Unstable")