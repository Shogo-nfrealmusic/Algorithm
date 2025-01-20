# # 入力
# N = int(input())
# H = list(map(int, input().split()))

# # 動的計画法
# dp = [ None ] * N
# dp[0] = 0
# for i in range(1, N):
# 	if i == 1:
# 		dp[i] = abs(H[i - 1] - H[i])
# 	if i >= 2:
# 		v1 = dp[i - 1] + abs(H[i - 1] - H[i])  # 1 個前の足場からジャンプするとき
# 		v2 = dp[i - 2] + abs(H[i - 2] - H[i])  # 2 個前の足場からジャンプするとき
# 		dp[i] = min(v1, v2)

# # 答えの出力
# print(dp[N - 1])

# # 入力
# N = int(input())

# # 動的計画法
# dp = [ None ] * (N + 1)
# for i in range(N + 1):
# 	if i <= 1:
# 		dp[i] = 1
# 	else:
# 		dp[i] = dp[i - 1] + dp[i - 2]

# # 答えの出力
# print(dp[N])

# 入力
N, S = map(int, input().split())
A = list(map(int, input().split()))

# 配列の初期化
dp = [ [ None ] * (S + 1) for i in range(N + 1) ]
dp[0][0] = True
for i in range(1, S + 1):
	dp[0][i] = False

# 動的計画法
for i in range(1, N + 1):
	for j in range(0, S + 1):
		if j < A[i - 1]:
			# j < A[i-1] のとき、カード i を選べない
			dp[i][j] = dp[i - 1][j]
		else:
			# j >= A[i-1] のとき、選ぶ / 選ばない 両方の選択肢がある
			if (dp[i - 1][j] == True or dp[i - 1][j - A[i - 1]] == True):
				dp[i][j] = True
			else:
				dp[i][j] = False

# 答えを出力
if dp[N][S] == True:
	print("Yes")
else:
	print("No")
 
 # 入力
N = int(input())
A = list(map(int, input().split()))

# 配列の初期化
dp1 = [ None ] * (N + 1)
dp2 = [ None ] * (N + 1)
dp1[0] = 0
dp2[0] = 0

# 動的計画法
for i in range(1, N + 1):
	dp1[i] = dp2[i - 1] + A[i - 1]
	dp2[i] = max(dp1[i - 1], dp2[i - 1])

# 出力
Answer = max(dp1[N], dp2[N])
print(Answer)