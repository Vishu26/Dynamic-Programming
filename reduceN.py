# reduce N

def dp(n,memo):
    if n<=1:
        return 0
    if memo[n]!=-1:
        return memo[n]
    f=0
    f=1 + dp(n - 1, memo)
    if n%2==0:
        f=min(dp(n//2,memo)+1,dp(n-1,memo)+1)
    if n%3==0:
        f=min(dp(n // 3,memo) + 1, dp(n - 1,memo) + 1)
    memo[n]=f
    return memo[n]

print(dp(16,[-1]*17))