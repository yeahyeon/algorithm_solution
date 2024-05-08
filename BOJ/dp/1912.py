n = int(input())
num = list(map(int, input().split()))
dp = num

for i in range(1,n):
    dp[i] = max(num[i],dp[i-1]+num[i])

print(max(dp))
