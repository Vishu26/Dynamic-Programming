def dp(a,n):
    ans=[[0]*n for i in range(n)]
    brac=[[0]*n for i in range(n)]
    for l in range(2,n):
        for i in range(1,n-l+1):
            j=i+l-1
            ans[i][j]=float('inf')
            for t in range(i,j):
                if ans[i][j]>ans[i][t]+ans[t+1][j]+a[i-1]*a[t]*a[j]:
                    ans[i][j] = ans[i][t] + ans[t + 1][j] + a[i - 1] * a[t] * a[j]
                    brac[i][j]=t
    paren = ''
    printBrac(brac,1,n-1,'A')
    print(paren)
    return ans[1][n-1]


def printBrac(brac,i,j,c):
    if i==j:
        print(c)
        c = chr(ord(c)+1)
    else:
        print('(')
        printBrac(brac,i,brac[i][j],c)
        printBrac(brac,brac[i][j]+1,j,c)
        print(')')



a = [40, 20, 30, 10, 30]
n=5
print(dp(a,n))
