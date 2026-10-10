# Champagne Tower

row = int(input("Enter row number: "))
glass = int(input("Enter glass number: "))

dp = [[0] * 10 for i in range(10)]

dp[0][0] = 1

for i in range(row):
    for j in range(i + 1):

        if dp[i][j] > 1:
            extra = (dp[i][j] - 1) / 2

            dp[i + 1][j] += extra
            dp[i + 1][j + 1] += extra

amount = min(1, dp[row][glass])

print("Champagne in the glass:", amount)