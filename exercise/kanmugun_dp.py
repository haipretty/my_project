#dp:动态规划
def rearrangeSticks(n: int, k: int) -> int:
    MOD = pow(10, 9) + 7
    dp = [[0]*(k+1) for _ in range(n+1)]
    dp[0][0] = 1

    for i in range(1, n+1):
        for j in range(1, min(i, k)+1):
            dp[i][j] = (dp[i-1][j-1] + (i-1)*dp[i-1][j]) % MOD
    
    return dp[n][k]

print(rearrangeSticks(5,3))

"""
dp[1][1]
dp[2][1] = dp[1][0] + dp[1][1]
"""