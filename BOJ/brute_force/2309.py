from itertools import combinations

arr = [int(input()) for _ in range(9)]
arr.sort()
combi = list(combinations(arr,2))

for i in combi:
    if sum(i) == sum(arr)-100:
        arr.remove(i[0])
        arr.remove(i[1])
        break

for i in arr:
    print(i)
