'''
알고리즘 순서 생각은 잘 했지만 구현에서 어려움을 겪었다.
특히 longest 함수 구현에서 애 먹었다.
꾸준히 문제를 풀어 구현 실력을 늘려야겠다.
'''

n = int(input())
candies = [list(map(str,input())) for _ in range(n)]
res = 0


# 먹을 수 있는 사탕 수를 세는 함수
def longest(candies):
    res = 1
    for i in range(n):
        cnt = 1
        for j in range(1,n):
            if candies[i][j] == candies[i][j-1]: # 행에서 최대 찾기 
                cnt += 1
            else:
                cnt = 1
            res = max(res,cnt)
        
        cnt = 1
        for j in range(1,n): #열에서 최대 찾기 
            if candies[j][i] == candies[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            res = max(res,cnt)

    return res

# 동일 행에서 바꾸는 경우 
for i in range(n):
    for j in range(n):
        # 열 
        if j+1<n:
            candies[i][j],candies[i][j+1] = candies[i][j+1],candies[i][j]
            cnt = longest(candies)
            res = max(res,cnt)
            candies[i][j],candies[i][j+1] = candies[i][j+1],candies[i][j]
        
        # 행 
        if i+1<n:
            candies[i][j],candies[i+1][j] = candies[i+1][j],candies[i][j]
            cnt = longest(candies)
            res = max(res,cnt)
            candies[i][j],candies[i+1][j] = candies[i+1][j],candies[i][j]
    
print(res)


