'''
<모험가 길드>
한 마을에 모험가가 N명 있습니다. 모험가 길드에서는 N명의 모험가를 대상으로 '공포도'를 측정했는데, '공포도'가 높은 모험가는
쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어집니다. 모험가 길드장인 영준이는 모험가 그룹을 안전하게 구성하고자
공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있도록 규정했습니다.
영준이는 최대 몇 개의 모험가 그룹을 만들 수 있는지 궁금합니다. 영준이를 위해 N명의 모험가에 대한 정보가 주어졌을 때,
여행을 떠날 수 있는 그룹 수의 최댓값을 구하는 프로그램을 작성하세요.
예를 들어 N = 5이고, 각 모험가의 공포도가 다음과 같다고 가정합시다.

2 3 1 2 2

이때, 그룹 1에 공포도가 1, 2, 3인 모험가를 한 명씩 넣고, 그룹 2에 공포도가 2인 남은 두 명을 넣게 되면, 총 2개의 그룹을
만들 수 있습니다. 또한 몇 명의 모험가는 마을에 그대로 남아 있어도 되기 때문에, 모든 모험가를 특정한 그룹에 넣을 필요는 없습니다.

<입력조건>
* 첫째 줄에 모험가의 수 N이 주어집니다.(1 <= N <= 100,000)
* 둘째 줄에 모험가의 공포도의 값을 N 이하의 자연수로 주어지며, 각 자연수는 공백으로 구분합니다.

<출력조건>
* 여행을 떠날 수 있는 그룹의 최댓값을 출력합니다.

<입력예시>     <출력예시>
5              2
2 3 1 2 2
'''
# 정수형 N값과 공포도를 list로 받음.
n = int(input())
data = list(map(int, input().split()))

# group의 개수를 받을 변수 선언
group = 0
# 데이터를 오름차순으로 정렬
data.sort()

while True:
    # 데이터에서 공포도가 가장 큰 값이 배열의 길이(최대 인원수)보다 크다면 마을에 남긴다.(즉 데이터를 버린다.)
    if max(data) > len(data):
        data.pop()
    else:
        # 가장 공포도가 큰 값부터 묶어준다.(여기서는 데이터를 제거한다.)(공포도가 낮을수록 그룹화하기 쉽기때문)
        for i in range(max(data)):
            data.pop()
        group += 1
    # 데이터가 비어있다면(모두 그룹화했다면) 반복문을 탈출한다.
    if len(data) == 0:
        break

# 그룹의 개수를 출력한다.
print(group)

# 위 풀이는 틀린풀이입니다.