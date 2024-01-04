"""
생각보다 간단한 문제지만 코드 구현이 아직 익숙하지 않았다.
푸는 방법은 맞췄으나, 구현하는 과정에서 헤맸다.
처음 작성한 코드는 정상적인 입력에 대해서는 제대로 작동했지만,
"NO"인 경우의 처리를 하지 못했다. (너무 복잡하게 생각했다)
그 이후로는 정답 코드를 참고하여 코드를 수정했다.
"""

n = int(input())
stack = []
res = []
state = 0
cnt = 1

for i in range(n):
    num = int(input())
    while cnt <= num: # cnt ~ 입력한 수 push
        stack.append(cnt)
        res.append("+")
        cnt += 1
    
    if stack[-1] == num: # stack의 top이 입력한 수와 같다면 pop한다
        stack.pop()
        res.append("-")
    else: # stack의 top이 입력한 수와 다르다면 실패
        state = 1
        break

if state == 0: # 성공적인 경우만 출력
    for i in res:
        print(i)
else:
    print("NO")

