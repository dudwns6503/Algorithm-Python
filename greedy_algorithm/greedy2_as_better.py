# 문제는 greedy2.py에 작성되어 있습니다.

n, m = map(int, input().split())

result = 0

for i in range(n):
  data = list(map(int, input().split()))
  # 현재 줄에서 가장 작은 수 찾기
  min_value = min(data)
  # '가장 작은 수'들 중에서 가장 큰 수 찾기
  result = max(result, min_value)

print(result)