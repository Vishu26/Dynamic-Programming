##### GREEDY SOLUTION #####
from itertools import accumulate
from bisect import bisect

def fracKnapsack(vl, wt, W, n):

    r = list(sorted(zip(vl,wt), key=lambda x:x[0]/x[1],reverse=True))
    vl , wt = [i[0] for i in r],[i[1] for i in r]
    acc=list(accumulate(wt))
    k = bisect(acc,W)
    return 0 if k == 0 else sum(vl[:k])+(W-acc[k-1])*(vl[k])/(wt[k]) if k!=n else sum(vl[:k])

print("%.0f"%fracKnapsack([60, 100, 120],[10, 20, 30],50,3))


'''def knapSack(W, wt, val, frac,n):
    K = [[0]*(W + 1)]*(n + 1)

    # Build table K[][] in bottom up manner
    for i in range(1,n + 1):
        for w in range(1,W + 1):
            if wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            elif frac[i-1]=='f':
                K[i][w] = K[i-1][wt[i-1]-w] + val[i-1]*(wt[i-1]-w)/wt[i-1]
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]

# Driver program to test above function
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
frac = ['f','f','f']
print(knapSack(W, wt, val,frac, n))

def knapsack(r, W, i):
    if i==0:
        if W - r[i][1] >=0:
            return r[i][0]
        elif r[i][2]=='f':
            return r[i][0]*(W)/r[i][1]
        else:
            return 0
    else:
        if W - r[i][1] >=0:
            q = max(knapsack(r,W-r[i][1],i-1)+r[i][0],knapsack(r,W,i-1))
        elif r[i][2] == 'f':
            return r[i][0]*(W)/r[i][1]
        else:
            return knapsack(r,W,i-1)
    return q

vl = [60,100,120]

wt = [10,20,30]

op = ['f','f','f']def knapSack(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
 
    # Build table K[][] in bottom up manner
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
 
    return K[n][W]
 
# Driver program to test above function
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapSack(W, wt, val, n))

W = 50

r = list(sorted(zip(vl,wt,op),key = lambda x:(x[0]/x[1], x[0])))

print(knapsack(r,W,2))'''