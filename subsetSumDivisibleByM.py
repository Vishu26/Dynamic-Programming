def dp(a,i,m,su):
    if su!=0 and su%m==0:
        return True
    if i==0:
        return ((su+a[i])%m)==0
    return dp(a,i-1,m,su) or dp(a,i-1,m,su+a[i])



print(dp([1, 7],1,5,0))