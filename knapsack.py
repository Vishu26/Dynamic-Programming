#####   NAIVE RECURSION #######

def dp (vl , wt , i , n, W , su):
    if i==n-1:
        if su+wt[i] <=W:
            return vl[i]
        return su
    else:
        if su + wt[i] <=W:
            return max(dp(vl,wt,i+1,n,W,su+wt[i])+vl[i],dp(vl,wt,i+1,n,W,su))
        else:
            return dp(vl,wt,i+1,n,W,su)



def knapsack(vl, wt, W, n):

    dp = [[0]*(W+1) for i in range(n+1)]

    for i in range(1,n+1):
        for w in range(1,W+1):
            if wt[i-1] < W:
                dp[i][w] = max(vl[i-1]+dp[i-1][w-wt[i-1]],dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][W]

print(knapsack([60, 100, 120],[10, 20, 30],50,3))