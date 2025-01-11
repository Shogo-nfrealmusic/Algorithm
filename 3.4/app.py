# 入力
N = int(input())
B = list(map(int, input().split()))
R = list(map(int, input().split()))

# 答えの計算（Python 3 では B[i] / N, R[i] / N は小数まで計算されることに注意）
blue = 0.0
red = 0.0
for i in range(N):
	blue += B[i] / N
	red += R[i] / N

# 出力
print("%.12f" % (blue + red))

# 入力
N = int(input())
P = [ None ] * N
Q = [ None ] * N
for i in range(N):
	P[i], Q[i] = map(int, input().split())

# 答えの計算（Python 3 では Q[i] / P[i] は小数まで計算されることに注意）
answer = 0
for i in range(N):
	answer += Q[i] / P[i]

# 出力
print("%.12f" % answer)

# 入力
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 答えを求める
Answer = 0.0
for i in range(N):
	Answer += (1.0 / 3.0) * A[i] + (2.0 / 3.0) * B[i]

# 出力
print("%.12f" % Answer)
# 入力
N = int(input())

# 答えの計算
Answer = 0.0
for i in range(1, N+1):
	Answer += 1.0 * N / i

# 出力
print("%.12f" % Answer)