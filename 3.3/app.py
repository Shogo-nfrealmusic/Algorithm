# 注意
# Python で提出すると、N = 100 では実行に 10 秒程度かかり、TLE（実行時間制限オーバー）になります。
# 一方、同じプログラムを PyPy3 で提出すると、実行に 0.5 秒程度しかかからず、AC（正解）することができます。

# 入力
# N = int(input())
# A = list(map(int, input().split()))

# # 5 つのカードの番号 (i, j, k, l, m) を全探索
# answer = 0
# for i in range(0, N):
# 	for j in range(i + 1, N):
# 		for k in range(j + 1, N):
# 			for l in range(k + 1, N):
# 				for m in range(l + 1, N):
# 					if A[i] + A[j] + A[k] + A[l] + A[m] == 1000:
# 						answer += 1

# # 出力
# print(answer)
# 入力
# n,r = map(int, input().split())

# # 階乗の計算
# fact_n = 1
# for i in range(1, n+1):
# 	fact_n *= i

# fact_r = 1
# for i in range(1, r+1):
# 	fact_r *= i

# fact_nr = 1
# for i in range(1, n-r+1):
# 	fact_nr *= i

# # 出力
# print(int(fact_n / (fact_r * fact_nr)))

# 入力
# N = int(input())
# A = list(map(int, input().split()))

# # 答えを求める
# a = 0
# b = 0
# c = 0
# d = 0
# for i in range(N):
# 	if A[i] == 100:
# 		a += 1
# 	if A[i] == 200:
# 		b += 1
# 	if A[i] == 300:
# 		c += 1
# 	if A[i] == 400:
# 		d += 1

# # 出力
# print(a * d + b * c)

# 入力
N = int(input())
A = list(map(int, input().split()))

# 答えを求める
cnt = [0 for i in range(100000)]
for i in range(N):
	cnt[A[i]] += 1

Answer = 0
for i in range(1, 50000):
	Answer += cnt[i] * cnt[100000 - i]
Answer += cnt[50000] * (cnt[50000] - 1) // 2

# 出力
print(Answer)