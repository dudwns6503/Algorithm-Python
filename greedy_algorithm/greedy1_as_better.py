# 문제는 greedy1.py에 작성되어 있습니다.

n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

# 위까진 greedy1.py 랑 동일

# 반복되는 수열에 대해서 파악을 해야 이 알고리즘을 이해할 수 있다.

count = int(m / (k + 1)) * k
count += m % (k + 1)              # count는 가장 큰 수가 더해지는 횟수

result = 0
result += (count) * first         # 가장 큰 수를 count 번 더한다.
result += (m - count) * second    # 그 다음 큰 수를 m - count 번 더한다.

print(result)
