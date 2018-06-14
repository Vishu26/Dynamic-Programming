def binomialCoeff(n , k):

    C = [0 for i in xrange(k+1)]
    C[0] = 1
 
    for i in range(1,n+1):
 
        j = min(i ,k)
        while (j>0):
            C[j] = C[j] + C[j-1]
            j -= 1
 
    return C[k]

n = 5
k = 2
print "Value of C(%d,%d) is %d" %(n,k,binomialCoeff(n,k))
