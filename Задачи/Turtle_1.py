def max_path_sum(n, m, table):
    dp = [[0] * m for _ in range(n)]

    dp[0][0] = table[0][0]
    for i in range(1, m):
        dp[0][i] = dp[0][i-1] + table[0][i]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + table[i][0]

    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = table[i][j] + max(dp[i-1][j], dp[i][j-1])

    return dp[n-1][m-1]

n, m = map(int, input().split())
table = []
for _ in range(n):
    row = list(map(int, input().split()))
    table.append(row)

result = max_path_sum(n, m, table)

print(result)
