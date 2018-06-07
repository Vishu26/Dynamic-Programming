# Print the number of AVL tree that can be constructed from given height

def dp(h):
    ans=[1]*(h+1)
    for i in range(2,h+1):
        ans[i]=ans[i-1]*(ans[i-1]+2*ans[i-2])
    return ans[h]

print(dp(19))