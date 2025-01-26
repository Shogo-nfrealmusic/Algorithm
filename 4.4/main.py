# # r = 2.0 # √2 を求めたいから
# # a = 2.0 # 初期値を適当に 2.0 にセットする
# # repeats = 5

# # for i in range(1, repeats + 1):
# # 	# 点 (a, f(a)) の x 座標と y 座標を求める
# # 	zahyou_x, zahyou_y = a, a * a
	
# # 	# 接線の式 y = sessen_a * x + sessen_b を求める
# # 	sessen_a = 2.0 * zahyou_x
# # 	sessen_b = zahyou_y - sessen_a * zahyou_x
	
# # 	# 次の a の値 next_a を求める
# # 	next_a = (r - sessen_b) / sessen_a
# # 	print("Step #%d: a = %.12f -> %.12f" % (i, a, next_a))
# # 	a = next_a
 
# # r = 2.0 # √2 を求めたいから
# # a = 2.0 # 初期値を適当に 2.0 にセットする
# # repeats = 5

# # for i in range(1, repeats + 1):
# # 	# 点 (a, f(a)) の x 座標と y 座標を求める
# # 	zahyou_x, zahyou_y = a, a * a * a
	
# # 	# 接線の式 y = sessen_a * x + sessen_b を求める
# # 	sessen_a = 3.0 * zahyou_x * zahyou_x
# # 	sessen_b = zahyou_y - sessen_a * zahyou_x
	
# # 	# 次の a の値 next_a を求める
# # 	next_a = (r - sessen_b) / sessen_a
# # 	print("Step #%d: a = %.12f -> %.12f" % (i, a, next_a))
# # 	a = next_a
 
# # l = 1.0
# # r = 2.0
# # repeats = 20

# # for i in range(1, repeats + 1):
# # 	m = (l + r) / 2.0
# # 	if m * m < 2.0:
# # 		l = m
# # 	else:
# # 		r = m
# # 	print("Step #%d: m = %.12f" % (i, m))
 
# #  # 初期設定
# # base = 10.0  # 底
# # exponent = 0.3  # 指数
# # approx = 1.0  # 初期値（近似値）
# # precision = 0.000001  # 許容誤差
# # iterations = 100  # 最大反復回数

# # # 四則演算のみで指数を計算
# # for _ in range(iterations):
# #     prev_approx = approx
# #     # 近似値を更新する式
# #     approx = approx * (1 + (exponent * (base / approx) - 1) / exponent)
    
# #     # 許容誤差内に収まったら終了
# #     if abs(approx - prev_approx) < precision:
# #         break

# # print("10^0.3 ≈ {:.12f}".format(approx))

# # 入力 → 配列 prime の初期化
# N = int(input())
# prime = [ True ] * (N + 1)

# # エラトステネスのふるい
# LIMIT = int(N ** 0.5)
# for i in range(2, LIMIT + 1):
# 	if prime[i] == True:
# 		# x = 2i, 3i, 4i, ... と、N 以下の間ループし続ける
# 		for j in range(2 * i, N + 1, i):
# 			prime[j] = False

# # N 以下の素数を小さい順に出力
# for i in range(2, N + 1):
# 	if prime[i] == True:
# 		print(i)
  

# N = 1000
# Answer = 0.0

# for i in range(N):
# 	x = 1.0 * (2 * i + 1) / (2 * N)
# 	value = 2.0 ** (x * x)
# 	Answer += value

# print("%.12f" % (Answer / N))

# total = 0
# N = 0

# # 合計が30を超えるまで繰り返す
# while total <= 30:
#     N += 1
#     total += 1 / N
    
#     # 進行状況を出力する（10000回ごとに表示）
#     if N % 10000 == 0:
#         print(f"N = {N}, Total = {total}")

# print(f"The answer is N = {N}")

import math

# 30を超えるNを計算
target = 30
gamma = 0.57721  # オイラー・マスケローニ定数
log_value = target - gamma
N = math.exp(log_value)  # e^(30 - gamma)

# 結果を整数に切り上げ
print(math.ceil(N))


