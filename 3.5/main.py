# import random

# N = 10000 # N は試行回数（適宜変更する）
# M = 0
# for i in range(N):
# 	px = random.random() # 0 以上 1 未満の乱数を生成（C++ のコード 3.5.1 では 0 以上 1 以下の乱数を生成しているが、ほとんど同じ）
# 	py = random.random() # 0 以上 1 未満の乱数を生成（C++ のコード 3.5.1 では 0 以上 1 以下の乱数を生成しているが、ほとんど同じ）
# 	# 原点からの距離は sqrt(px * px + py * py)
# 	# これが 1 以下であれば良いので、条件は「px * px + py * py <= 1」（「sqrt(px * px + py * py) <= 1」と同値）
# 	if px * px + py * py <= 1.0:
# 		M += 1

# print("%.12f" % (4 * M / N))

import random

N = 1000000 # N は試行回数（適宜変更する）
M = 0
for i in range(N):
	px = 6.0 * random.random()
	py = 9.0 * random.random()
	
	# 点 (3, 3) との距離。この値が 3 以下であれば半径 3 の円に含まれる。
	dist_33 = ((px - 3.0) * (px - 3.0) + (py - 3.0) * (py - 3.0)) ** 0.5
	
	# 点 (3, 7) との距離。この値が 2 以下であれば半径 2 の円に含まれる。
	dist_37 = ((px - 3.0) * (px - 3.0) + (py - 7.0) * (py - 7.0)) ** 0.5
	
	# 判定
	if (dist_33 <= 3.0 or dist_37 <= 2.0):
		M += 1

print(M)