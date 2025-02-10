N = int(input())
if N % 2 == 0:
	print("Yes")
else:
	print("No")
 
 # 入力 → 数列の要素の総和 S を求める
N, K = map(int, input().split())
A = list(map(int, input().split()))
S = sum(A)

# 答えの出力
if S % 2 != K % 2:
	print("No")
elif S > K:
	print("No")
else:
	print("Yes")
 
 # 入力
H, W = map(int, input().split())

# 場合分け
if H == 1 or W == 1:
	print(1)
else:
	print((H * W + 1) // 2)
 
 # 入力
H, W = map(int, input().split())
A = [[] for i in range(H)]
for i in range(H):
	A[i] = list(map(int, input().split()))

# 行の総和を計算する
gyou = [0 for i in range(H)]
for i in range(H):
	for j in range(W):
		gyou[i] += A[i][j]

# 列の総和を計算する
retu = [0 for i in range(W)]
for j in range(W):
	for i in range(H):
		retu[j] += A[i][j]

# 各マスに対する答えを計算する
Answer = [[0 for j in range(W)] for i in range(H)]
for i in range(H):
	for j in range(W):
		Answer[i][j] = gyou[i] + retu[j] - A[i][j]

# 出力
for i in range(H):
	print(*Answer[i])
 
 # 最大公約数を返す関数
def GCD(A, B):
	while A >= 1 and B >= 1:
		if A < B:
			B = B % A  # A < B の場合、大きい方 B を書き換える
		else:
			A = A % B  # A >= B の場合、大きい方 A を書き換える
	if A >= 1:
		return A
	return B

# 最小公倍数を返す関数
def LCM(A, B):
	return int(A / GCD(A, B)) * B

# 入力
N, K = map(int, input().split())
V = list(map(int, input().split()))

# ビット全探索
Answer = 0
for i in range(1, 1 << K):
	cnt = 0
	lcm = 1
	for j in range(K):
		if (i & (1 << j)) != 0:
			cnt += 1
			lcm = LCM(lcm, V[j])
			
	# num は N 以下の中で選ばれたすべての倍数であるものの個数
	num = N // lcm
	if cnt % 2 == 1:
		Answer += num
	else:
		Answer -= num

# 出力
print(Answer)