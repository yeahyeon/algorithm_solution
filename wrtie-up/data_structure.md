### 스택(stack)

![Untitled](%E1%84%8C%E1%85%A1%E1%84%85%E1%85%AD%E1%84%80%E1%85%AE%E1%84%8C%E1%85%A9%20ed82690547004c06991690e07464db9d/Untitled.png)

한 쪽 끝에서만 자료를 넣고 빼는 작업이 이루어지는 자료구조

LIFO(Last In First Out) 방식으로 동작하며 가장 최근 삽입된 자료의 위치를 **top**이라고 한다.

**[기본 연산]**

- `stack.push`: top에 새로운 데이터 삽입
- `stack.pop`: 가장 최근에 삽입된 데이터 삭제
- `stack.top`: 가장 최근에 삽입된 데이터

**[시간복잡도]**

시간복잡도는 top에서 바로 데이터에 접근할 수 있기 때문에 **O(1)**

**[라이브러리]**

파이썬 내장모듈로 따로 존재하지 않는다. 보통 deque 라이브러리를 스택 대신 사용한다.

`append()`, `pop()` 메서드를 활용한다.

### 큐 (Queue)

![Untitled](%E1%84%8C%E1%85%A1%E1%84%85%E1%85%AD%E1%84%80%E1%85%AE%E1%84%8C%E1%85%A9%20ed82690547004c06991690e07464db9d/Untitled%201.png)

양쪽 끝에서 데이터의 삽입과 삭제가 이루어지는 자료구조. FIFO (First In First Out)으로 동작한다.

데이터가 삽입되는 곳이 **rear**, 데이터가 제거되는 곳이 **front**이다.

데이터를 삭제하기 전에 큐가 empty한지, 추가할 때는 큐가 full인지 확인하고 진행해야한다.

**[선형 큐(linear queue)]**

![Untitled](%E1%84%8C%E1%85%A1%E1%84%85%E1%85%AD%E1%84%80%E1%85%AE%E1%84%8C%E1%85%A9%20ed82690547004c06991690e07464db9d/Untitled%202.png)

선형 배열을 사용하여 구현된 queue.

삽입을 위해 계속 요소를 이동시켜야 한다. front, rear는 증가만 하여 front 앞에 공간이 있어도 삽입할 수 없는 경우가 발생할 수 있다.

**[원형 큐(circular queue)]**

![Untitled](%E1%84%8C%E1%85%A1%E1%84%85%E1%85%AD%E1%84%80%E1%85%AE%E1%84%8C%E1%85%A9%20ed82690547004c06991690e07464db9d/Untitled%203.png)

- front: 맨 첫번째 요소 바로 앞
- rear: 마지막 요소
- empty 상태: front == rear
- full 상태: front == (rear+1) % MAX_QUEUE_SIZE

**[시간복잡도]**

front, rear의 위치로 데이터 삽입 삭제가 바로 이루어지기 때문에 **O(1)**

**[라이브러리]**

- list: 시간복잡도가 O(n)이기 때문에 유의
- queue 모듈의 Queue 클래스: `put(x)`, `get()` 메서드 활용. 하지만 인덱스로 접근 불가
- collections 모듈의 의 deque 클래스: `popleft(x)`, `appendleft(x)` 메서드 활용

### 덱(Deque)

![Untitled](%E1%84%8C%E1%85%A1%E1%84%85%E1%85%AD%E1%84%80%E1%85%AE%E1%84%8C%E1%85%A9%20ed82690547004c06991690e07464db9d/Untitled%204.png)

양쪽 (front, rear)에서 삽입과 삭제가 가능한 큐를 의미하는 자료구조

가변적 크기를 가진다. chunk 된 메모리 형태로 군데군데 흩어져있다.

중간에 데이터가 삽입될 때 다른 요소들을 앞, 뒤로 밀 수 있다. (다만 성증은 안 좋음)

**[시간복잡도]**

삽입, 삭제, 탐색 **O(1)**

**[라이브러리]**

collections 모듈의 deque 클래스 활용. 

덱을 확장하고 싶을 때 `extend()`, `extendleft()` 메서드를 이용한다.

리스트처럼 사용할 수도 있다 (`insert()`, `remove()`, `reverse()`)
