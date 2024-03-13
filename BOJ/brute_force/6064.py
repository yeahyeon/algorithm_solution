import sys
import math
input = sys.stdin.readline

def k(m,n,x,y):
    while x<=m*n: #maximum of the year is m*n
        if(x-y)%n == 0:
            return x
        x += m
    return -1

t = int(input())
for _ in range(t):
    m,n,x,y = map(int,input().split())
    print(k(m,n,x,y))

# 문제를 푸는 수식을 알아내는 과정은 쉬웠으나,
# 시간복잡도를 고려하여 코드를 짜는 것에 막혔다.


