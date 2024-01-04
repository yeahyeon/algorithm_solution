"""
문제만 두고 봤을 때는 어렵지 않은데,
시간 제한이 0.3초 밖에 안되는 문제이다.
내장 함수들의 시간복잡도를 잘 고려하여 풀어야한다.
시간 초과로 여러번 실패했다.
꾸준히 문제들을 풀며 감을 더 쌓아가야겠다.
"""

import sys

str_l= list(input())
str_r = []
m = int(input())

for _ in range(m):
    command = sys.stdin.readline().split()

    if command[0]=="L" and str_l:
        str_r.append(str_l.pop())
    
    elif command[0]=="D" and str_r:
        str_l.append(str_r.pop())
        
    elif command[0] == "B" and str_l:
        str_l.pop()

    elif command[0] == "P":
        str_l.append(command[1])

print("".join(str_l + list(reversed(str_r))))
