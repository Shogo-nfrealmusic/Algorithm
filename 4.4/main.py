r = 2.0 # √2 を求めたいから
a = 2.0 # 初期値を適当に 2.0 にセットする
repeats = 5

for i in range(1, repeats + 1):
	# 点 (a, f(a)) の x 座標と y 座標を求める
	zahyou_x, zahyou_y = a, a * a
	
	# 接線の式 y = sessen_a * x + sessen_b を求める
	sessen_a = 2.0 * zahyou_x
	sessen_b = zahyou_y - sessen_a * zahyou_x
	
	# 次の a の値 next_a を求める
	next_a = (r - sessen_b) / sessen_a
	print("Step #%d: a = %.12f -> %.12f" % (i, a, next_a))
	a = next_a
 
r = 2.0 # √2 を求めたいから
a = 2.0 # 初期値を適当に 2.0 にセットする
repeats = 5

for i in range(1, repeats + 1):
	# 点 (a, f(a)) の x 座標と y 座標を求める
	zahyou_x, zahyou_y = a, a * a * a
	
	# 接線の式 y = sessen_a * x + sessen_b を求める
	sessen_a = 3.0 * zahyou_x * zahyou_x
	sessen_b = zahyou_y - sessen_a * zahyou_x
	
	# 次の a の値 next_a を求める
	next_a = (r - sessen_b) / sessen_a
	print("Step #%d: a = %.12f -> %.12f" % (i, a, next_a))
	a = next_a
 
l = 1.0
r = 2.0
repeats = 20

for i in range(1, repeats + 1):
	m = (l + r) / 2.0
	if m * m < 2.0:
		l = m
	else:
		r = m
	print("Step #%d: m = %.12f" % (i, m))
 
 # 初期設定
base = 10.0  # 底
exponent = 0.3  # 指数
approx = 1.0  # 初期値（近似値）
precision = 0.000001  # 許容誤差
iterations = 100  # 最大反復回数

# 四則演算のみで指数を計算
for _ in range(iterations):
    prev_approx = approx
    # 近似値を更新する式
    approx = approx * (1 + (exponent * (base / approx) - 1) / exponent)
    
    # 許容誤差内に収まったら終了
    if abs(approx - prev_approx) < precision:
        break

print("10^0.3 ≈ {:.12f}".format(approx))

