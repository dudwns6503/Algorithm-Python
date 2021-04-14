'''
<부품 찾기>
영준이네 전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다. 어느 날 손님이 M개 종류의 부품을
대량으로 구매하겠다며 당일 날 견적서를 요청했다. 영준이는 때를 놓치지 않고 손님이 문의한 부품 M개 종류를 모두 확인해서
견적서를 작성해야 한다. 이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자.

예를 들어 가게의 부품이 총 5개일 때 부품번호가 다음과 같다고 하자.
N = 5
[8, 3, 7, 9, 2]

손님은 총 3개의 부품이 있는지 확인 요청했는데 부품 번호는 다음과 같다.
M = 3
[5, 7, 9]

이때 손님이 요청한 부품 번호의 순서대로 부품을 확인해 부품이 있으면 yes를, 없으면 no를 출력한다. 구분은 공백으로 한다.

<입력조건>
* 첫째 줄에 정수 N이 주어진다. (1 <= N <= 1,000,000)
* 둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다. 이때 정수는 1보다 크고, 1,000,000 이하이다.
* 셋째 줄에는 정수 M이 주어진다. (1 <= M <= 100,000)
* 넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다. 이때 정수는 1보다 크고, 1,000,000 이하이다.

<출력조건>
* 첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes를, 없으면 no를 출력한다.

<입력예시>     <출력예시>
5              no yes yes
8 3 7 9 2
3 
5 7 9
'''

# 이진탐색 함수 선언
def binary_search(array, target, start, end):
    # 데이터가 없다면 None을 반환
    if start > end:
        return None
    # 중간 인덱스 설정
    mid = (start + end) // 2
    
    # 데이터가 있다면 인덱스를 반환한다.
    if array[mid] == target:
        return mid
    # 중간 인덱스에 있는 값이 찾는 값보다 크다면 왼쪽을 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # 중간 인덱스에 있는 값이 찾는 값보다 작다면 오른쪽 값을 확인
    else:
        return binary_search(array, target, mid+1, end)


n = int(input())
array1 = list(map(int, input().split()))
# 값을 정렬해주어야 이진탐색 가능
array1.sort()

m = int(input())
array2 = list(map(int, input().split()))

# array2에 있는 배열 원소를 이진탐색
for i in array2:
    result = binary_search(array1, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

