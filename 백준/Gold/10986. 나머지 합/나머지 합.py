# 입력 받기
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 누적 합 배열과 나머지 배열 초기화
prefix_sum = [0] * (n + 1)
remainder_count = [0] * m
prefix_sum[0] = 0
remainder_count[0] = 1  # 초기값 설정

# 누적 합과 나머지 배열 계산
for i in range(1, n + 1):
    prefix_sum[i] = (prefix_sum[i - 1] + arr[i - 1]) % m
    remainder_count[prefix_sum[i]] += 1

# 결과 계산
result = 0
for count in remainder_count:
    result += count * (count - 1) // 2

# 결과 출력
print(result)
