### Find the longest common subsequence between two arrays/strings ###

def dp(a,b,n,m):
    lcs=[[0]*(m+1) for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i-1]==b[j-1]:
                lcs[i][j]=lcs[i-1][j-1]+1
            else:
                lcs[i][j]=max(lcs[i-1][j],lcs[i][j-1])
    print("Length of the longest common subsequence : "+str(lcs[n][m]))
    print("One of such longest common subsequence : ",end="")
    i,j=n,m
    while i>0 and j>0:
        if a[i-1]==b[j-1]:
            yield a[i-1]
            ind-=1
            j-=1
            i-=1
        elif lcs[i-1][j]>lcs[i][j-1]:
            i-=1
        else:
            j-=1