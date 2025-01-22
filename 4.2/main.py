# N, Q = map(int, input().split())
# A = list(map(int, input().split()))
# L = [ None ] * Q
# R = [ None ] * Q
# for j in range(Q):
# 	L[j], R[j] = map(int, input().split())

# B = [ None ] * (N + 1)
# B[0] = 0
# for i in range(N):
# 	B[i + 1] = B[i] + A[i]

# for j in range(Q):
# 	print(B[R[j]] - B[L[j] - 1])
 
 # 入力
# N, Q = map(int, input().split())
# L = [ None ] * Q
# R = [ None ] * Q
# X = [ None ] * Q
# for i in range(Q):
# 	L[i], R[i], X[i] = map(int, input().split())

# # 階差の計算
# B = [ 0 ] * (N + 2)
# for i in range(Q):
# 	B[L[i]] += X[i]
# 	B[R[i] + 1] -= X[i]

# # 答えを計算して出力
# answer = ""
# for i in range(2, N + 1):
# 	if B[i] > 0:
# 		answer += "<"
# 	if B[i] == 0:
# 		answer += "="
# 	if B[i] < 0:
# 		answer += ">"
# print(answer)

# 入力
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = [0 for i in range(M)]
for i in range(M):
	B[i] = int(input())

# 累積和をとる
S = [0 for i in range(N)]
for i in range(1, N):
	S[i] = S[i - 1] + A[i - 1]

# 答えを求める
# B[i] - 1 などになっているのは、配列の index が 0 始まりだから
Answer = 0
for i in range(M-1):
	if B[i] < B[i + 1]:
		Answer += S[B[i + 1] - 1] - S[B[i] - 1]
	else:
		Answer += S[B[i] - 1] - S[B[i + 1] - 1]

# 出力
print(Answer)

# 入力
T = int(input())
N = int(input())
A = [0 for i in range(T + 2)]
B = [0 for i in range(T + 2)]
L = [0 for i in range(N)]
R = [0 for i in range(N)]
for i in range(N):
	L[i], R[i] = map(int, input().split())

# 階差 B[i] を計算する
for i in range(N):
	B[L[i]] += 1
	B[R[i]] -= 1

# 累積和 A[i] を計算する
A[0] = B[0]
for i in range(1, T):
	A[i] = A[i - 1] + B[i]

# 出力
for i in range(T):
	print(A[i])