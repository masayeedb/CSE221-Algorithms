#Task 4

def mcoin(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

input_data = open("input4.txt", "r")
output_data = open("output4.txt", "w")

N, X = map(int, input_data.readline().split())
coins = list(map(int, input_data.readline().split()))
output_data.write(str(mcoin(coins, X)))

input_data.close()
output_data.close()