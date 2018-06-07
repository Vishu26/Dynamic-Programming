### Find the maximum price generated on cutting rod ###

def dp(a,n):
    r=[0]*(n+1)
    s=[0]*(n+1)
    for j in range(1,n+1):
        q=-1
        for i in range(1,j+1):
            if q<a[i-1]+r[j-i]:
                q=a[i-1]+r[j-i]
                s[j]=i
        r[j]=q
    print("The maximum price is : "+str(r[n]))
    print('Pieces are of length : ',end="")
    while n>0:
        yield s[n]
        n-=s[n]
for i in dp([3,7,8,8,10],5):
    print(i,end=" ")