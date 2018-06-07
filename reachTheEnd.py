#Count the minimum number of jumps from starting to reach the end

def dp(a,n):
    ans=[0]*n
    for i in range(1,n):
        ans[i]=10**5
        for j in range(i):
            if i<=j+a[j] and ans[j]!=10**5:
                ans[i]=min(ans[i],ans[j]+1)
    return ans[n-1]

print(dp([1, 3, 6, 1, 0, 9],6))