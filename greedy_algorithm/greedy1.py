"""
<큰 수의 법칙>
큰 수의 법칙은 일반적으로 통계 분야에서 다루어지는 내용이지만 동빈이는 본인만의 방식으로 다르게 사용하고 있다.
동빈이의 큰 수의 법칙은 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특성이다.
예를 들어 순서대로 2, 4, 5, 6으로 이루어진 배열이 있을 때 M이 8이고, K가 3이라고 가정하자. 이 경우 특정한 인덱스의 수가 연속해서
세 번까지만 더해질 수 있으므로 큰 수의 법칙에 따른 결과는 6 + 6 + 6 + 5 + 6 + 6 + 6 + 5 인 46이 된다. 단, 서로 다른 인덱스에 해당하는
수가 같은 경우에도 서로 다른 것으로 간주한다. 예를 들어 순서대로 3, 4, 3, 4, 3으로 이루어진 배열이 있을 때 M이 7이고, K가 2라고 가정하자.
이 경우 두 번째 원소에 해당하는 4와 네 번째 원소에 해당하는 4를 번갈아 두 번씩 더하는 것이 가능하다. 결과적으로
4 + 4 + 4 + 4 + 4 + 4 + 4 + 4 인 28이 도출된다.

<입력조건>
- 배열의 크기 N, 숫자가 더해지는 M, 그리고 K가 주어질 때 동빈이의 큰 수의 법칙에 따른 결과를 출력하시오.
(2 <= N <= 1,000), M(1 <= M <= 10,000), K(1 <= K <= 10,000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
- 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10,000 이하의 수로 주어진다.
- 입력으로 주어지는 K는 항상 M보다 작거나 같다.

<출력조건>
- 첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.

<입력예시>
5 8 3
2 4 5 4 6 
<출력예시>
46
"""

# 코드 부분

# N, M, K를 공백으로 구분하고 map을 이용하여 모든 원소에 int() 함수를 적용한다.
n, m, k = map(int, input().split())  

# 각 데이터를 공백으로 구분하여 입력한다.(이 문제에선 데이터의 수 = N)
data = list(map(int, input().split()))

data.sort()  # 데이터를 오름차순으로 정렬
first = data[n-1] # 가장 큰 수는 배열의 마지막 인덱스
second = data[n-2] # 그 다음 큰 수는 마지막 인덱스에서 -1 

result = 0

while True:
  # K번 가장 큰 수가 더해져야한다.
  for i in range(k): 
    if m == 0: # m이 0 즉, 모든 숫자를 다 더 했다면 반복문 탈출
      break
    result += first  # result에 가장 큰 수를 더한다.(K번 반복)
    m -= 1           # 더할 때마다 m을 -1 해준다.
  if m == 0:         
    break
  result += second   # 그 후 두번째로 큰 숫자를 1번 더해준다.
  m -= 1

print(result)   # 결과를 출력한다.