"""
<숫자 카드 게임>
숫자 카드 게임은 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임이다.
단, 게임의 룰을 지키며 카드를 뽑아야 하고 룰은 다음과 같다.

1. 숫자가 쓰인 카드들이 N x M 형태로 놓여 있다. 이때 N은 행의 개수를 의미하며, M은 열의 개수를 의미한다.
2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
3. 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
4. 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여
   최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다. 

<입력조건>
- 첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주어진다.
- 둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1 이상 10,000 이하의 자연수이다.
- 첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.

<출력조건>
- 첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.

<입력예시>     <출력예시>     <입력예시>     <출력예시>
3 3            2              2 4            3
3 1 2                         7 3 1 8
4 1 4                         3 3 3 4
2 2 2
"""

# 행, 열 입력을 받을 변수 선언
n, m = map(int, input().split())

# 리스트 입력을 받을 변수 선언
a = []
# 각 행에서 최솟값을 담을 변수
result = 0
# 각 행의 최솟값중 최댓값을 저장할 변수
b = 0
# 첫행부터 시작
for i in range(n):
  # 행의 개수만큼 반복하며 리스트의 데이터를 받는다.
  a = list(map(int, input().split())) 
  # 첫열부터 값 확인
  for j in range(m):
  # 맨 처음은 값을 넣어주기 위해서 예외를 둠.
    if (result == 0):
      result = a[j]
  # 앞 뒤 비교 및 제일 처음은 맨 앞쪽과 맨 뒤 비교(비효율적임)
    elif (a[j-1] <= a[j]):
      result = a[j-1]
  # 각 행에서 뽑은 값들을 비교
  if (result > b):
    b = result
print(b)