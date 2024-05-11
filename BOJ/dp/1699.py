n = int(input())        
dp = [i for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,i):
        if j*j > i:
            break
        if dp[i] > dp[i-j*j] + 1: #dp[i-j*j]에 j*j를 더한 것이므로 +1가지
            dp[i] = dp[i-j*j] + 1

print(dp[n])
