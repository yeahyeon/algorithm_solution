import sys
input = sys.stdin.readline

n = int(input())
d = [[0]*10 for _ in range(n)]
d[0] = [0,1,1,1,1,1,1,1,1,1]

for i in range(1,n):
    d[i][0] = d[i-1][1] # ends with 0
    d[i][9] = d[i-1][8] # ends with 9

    for k in range(1,9): # ends with 1~8
        d[i][k] = d[i-1][k-1] + d[i-1][k+1]
    
print(sum(d[n-1])%1000000000)
