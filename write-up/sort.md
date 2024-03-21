### 정렬 알고리즘

데이터를 특정한 기준에 따라서 순서대로 나열하는 것

1. **선택 정렬**
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/7b9ad4ef-cee1-4140-b4b3-73f5725d94a9/dff80f39-ea80-4059-99d1-3300af329895/Untitled.png)
    
    - 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그 다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복하는 것. ‘매번 가장 작은 것을 선택’한다.
    - 선택 정렬 소스코드
        
        ```python
        array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
        
        for i in range(len(array)):
        	min_index = i # 가장 작은 원소의 인덱스
        	for j in range(i+1, len(array)):
        		if array[min_index] > array[j]:
        			min_index = j
        		array[i]. array[min_index] = array[min_index], array[i] # 스와프
        
        print(array)
        ```
        
    - 선택 정렬의 시간 복잡도: $O(N^2)$
    - 다른 정렬 알고리즘들에 비해 비효율적인 편
2. **삽입 정렬**
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/7b9ad4ef-cee1-4140-b4b3-73f5725d94a9/7c6b1715-ad34-4ed7-95a0-027c69bee9af/Untitled.png)
    
    - 데이터가 거의 정렬되어 있을 때 훨씬 효율적인 정렬 방법 (거의 정렬되어 있다면 퀵 정렬보다 더 효율적이다)
    - 특정한 데이터를 적절한 위치에 ‘삽입’
    - 삽입 정렬 소스코드
        
        ```python
        array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
        
        for i in range(1, len(array)):
        	for j in range(i, 0, -1): # 인덱스 i부터 1까지 감소하여 반복
        		if array[j] < array[j-1]: # 한 칸씩 왼쪽으로 이동
        			array[j], array[j-1] = array[j-1], array[j]
        		else:
        			break
        
        print(array)
        ```
        
    - 삽입 정렬의 시간 복잡도: $O(N^2)$이지만 최선의 경우 $O(N)$
3. **퀵 정렬**
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/7b9ad4ef-cee1-4140-b4b3-73f5725d94a9/99b058bb-d6e7-40e0-b340-75a82a016622/Untitled.png)
    
    - 가장 많이 사용되는 알고리즘
    - 기준(pivot)을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작.
    리스트의 왼쪽에서 pivot보다 큰 수, 리스트의 오른쪽에서 pivot보다 작은 수를 순차적으로 찾아 위치를 바꾼다. (pivot은 리스트의 첫 번째 수라고 가정)
    왼쪽과 오른쪽이 서로 교차하면 pivot을 이동시킨다. (pivot의 왼쪽에는 pivot보다 작은 수만 오도록, pivot의 오른쪽에는 pivot보다 큰 수만 오도록)
        
        pivot을 기준으로 리스트를 분할하여 정렬이 완료될 때까지 위 작업을 반복 수행한다 .
        
    - 퀵 정렬 소스코드
        
        ```python
        array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
        
        def quick_sort(array, start, end):
        	if start <= end: #원소가 1개인 경우 종료
        		return
        	pivot = start
        	left = start + 1
        	right = end
        	while left < right:
        		#피벗보다 큰 데이터를 찾을 때까지 반복
        		while left <= end and array[left] <= array[pivot]:
        			left += 1
        		#피벗보다 작은 데이터를 찾을 때까지 반복
        		while right > start and array[right] >= array[pivot]: 
        			right -= 1
        		if left > right: #엇갈렸다면 작은 데이터와 피벗을 교체
        			array[right], array[pivot] = array[pivot], arary[right]
        		else: #엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        			array[left], array[right] = array[right], array[left]
        		
        quick_sort(array, 0, len(array)-1)
        print(array)
        ```
        
    - 퀵 정렬의 시간 복잡도: 평균 $O(NlogN)$이지만 최악의 경우 $O(N^2)$ (이미 데이터가 정렬되어 있는 경우)
    (기본 정렬 라이브러리를 사용하면 평균 시간복잡도를 보장해준다.)
4. **병합 정렬**
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/7b9ad4ef-cee1-4140-b4b3-73f5725d94a9/226de775-36eb-4502-ba37-b6d6b5d28022/Untitled.png)
    
5. **계수 정렬**
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/7b9ad4ef-cee1-4140-b4b3-73f5725d94a9/227c0944-384a-4763-9bbb-1c5dea2c1b7c/Untitled.png)
    
    - 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘
    - 데이터의 크기 범위가 제한되어 정수로 표현될 때만 사용 가능
    (ex. 데이터의 값이 무한한 범위를 가질 수 있는 실수형 데이터가 주이지는 경우 → 사용 x
     ex. 데이터의 개수가 N, 데이터 중 최댓값이 K일 때 → 사용 O)
        
        일반적으로 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000을 넘지 않을 때
        
    - 별도의 리스트를 선언하고 그 안에 정렬에 대한 정보를 담는 형식
        
        리스트의 인덱스가 정렬할 데이터의 모든 범위를 포함할 수 있게 하고, 정렬하고 싶은 데이터의 값과 동일한 인덱스의 데이터를 1씩 증가시킨다.
        
    - 계수 정렬 소스코드
        
        ```python
        #모든 원소의 값이 0보다 크거나 같다고 가정
        array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
        #모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
        count = [0] * (max(array)+1)
        
        for i in range(len(array)):
        	count[array[i]] += 1 #각 데이터에 해당하는 인덱스의 값 증가
        	
        for i in range(len(array)): #리스트에 기록된 정렬 정보 확인
        	for j in range(count[i]):
        		print(i, end = ' ') #띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
        ```
        
    - 계수 정렬의 시간 복잡도: $O(N+K)$
    - 계수 정렬의 공간 복잡도: $O(N+K)$

### 파이썬의 정렬 라이브러리

파이썬은 기본 정렬 라이브러리인 `sorted()` 함수를 제공한다. `sorted()`는 퀵 정렬과 동작 방식이 비슷한 병합 정렬을 기반으로 만들어졌는데, 병합 정렬은 일반적으로 퀵 정렬보다 느리지만 최악의 경우에도 시간 복잡도 $O(NlogN)$을 보장한다는 특징이 있다.

반환 결과는 리스트 자료형이다.

코딩 테스트에서 정렬 알고리즘이 사용되는 경우를 일반적으로 3가지 문제 유형으로 나눌 수 있다.

1. **정렬 라이브러리로 풀 수 있는 문제**: 단순히 정ㄹ려 기법을 알고 있는지 물어보는 문제로 기본 정렬 라이브러리의 사용 방법을 숙지하고 있으면 어렵지 않게 풀 수 있다.
2. **정렬 알고리즘의 원리에 대해서 물어보는 문제:** 선택 정렬, 삽입 정렬, 퀵 정렬 등의 원리르 ㄹ알고 있어야 문제를 풀 수 있다.
3. **더 빠른 정렬이 필요한 문제:** 퀵 정렬 기반의 정렬 기법으로는 풀 수 없으며 계수 정렬 등의 다른 정렬 알고리즘을 이용하거나 문제에서 기존에 알려진 알고리즘의 구조적인 개선을 거쳐야 풀 수 있다.
