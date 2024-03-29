import sys
input = sys.stdin.readline

n = int(input())
price = list(map(int,input().split()))
d = [0] * (n+1)

for i in range(1,n+1):
    d[i] = price[i-1] #initialize equal to the price

for i in range(2,n+1):
    for j in range(1,i):
        #compare which is the bigger case
        #when Mingyu has i-j cards, buy j more cards to make i cards
        d[i] = max(d[i],d[i-j]+price[j-1])

print(d[n])
