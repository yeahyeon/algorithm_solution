n = int(input())
a = list(map(int,input().split()))

dp = [1] * n    

for i in range(1,n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j]+1) #a[i]를 마지막 값으로 가지는 가장 긴 증가부분수열의 길이

print(max(dp))

#dp 배열에 저장된 수가 곧 자신이 dp[i]번째로 큰 숫자임을 의미하므로 n번째~1번째까지 출력해주면 된다.
seq = []
order = max(dp)
for i in range(n-1,-1,-1):
    if dp[i] == order:
        seq.append(a[i])
        order -= 1
seq.reverse()
for i in seq:
    print(i,end=' ')
