# Print the max stolen value from houses if adjacent houses cant be robbed simultaneously

def dp(a,n):

    ans=[0]*n
    ans[0]=a[0]
    ans[1]=max(a[1],a[0])
    for i in range(2,n):
        ans[i]=max(ans[i-2]+a[i],ans[i-1])
    return ans[n-1]

print(dp([5, 3, 4, 11, 2],5))