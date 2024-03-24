import sys
input = sys.stdin.readline

n = int(input())
l = [[int(input()),i] for i in range(n)] #[값,인덱스] 입력 받기
sorted_l = sorted(l) #정렬된 l
move = [] #움직여야하는 횟수를 담는 리스트 (몇 번의 소트를 거쳐야하는지)
for i in range(n):
    move.append(sorted_l[i][1] - l[i][1])

print(max(move)+1) #최대로 움직이는 횟수가 시행하는 버블 소트의 횟수

#시간초과 안뜨려고 최대한 노력해도 계속 시간 초과가 떠서 결국 검색해봤다
#이걸 어떻게 생각해내지...
