'''
시간복잡도를 고려하지 않고 풀었더니 시간 초과가 뜬다.
브루트포스로도 풀 수 있지만 시간복잡도를 고려하여 수학적 기믹을 적용시켜야하는 문제.
수학적 기믹 자체는 어렵지 않았다.
'''

e,s,m = map(int,input().split())

year = 1
while True:
    if((year-e)%15==0 and (year-s)%28==0 and (year-m)%19==0):
        break
    else:
        year+=1

print(year)
