'''
<소수 구하기>
M 이상 N 이하의 소수를 모두 출력하는 프로그램을 작성하시오.

<입력조건>
* 첫째 줄에 자연수 M과 N이 빈칸을 사이에 두고 주어진다.(1 <= M <= N <= 1,000,000)
* 단, M 이상 N 이하의 소수가 하나 이상 있는 입력만 주어진다.

<출력조건>
* 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

<입력예시>     <출력예시>
3 16           3
               5
               7
               11
               13         
'''

import math

# M과 N 입력받기
m, n = map(int, input().split())
# 처음에는 모든 수가 소수인 것으로 초기화
array = [True for i in range(1000001)]
# 1은 소수가 아니다.
array[1] = 0

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인하며
    if array[i] == True: # i가 소수라면 i를 제외한 모든 배수를 제거하기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

# M부터 N까지의 모든 소수 출력
for i in range(m, n + 1):
    if array[i]:
        print(i)