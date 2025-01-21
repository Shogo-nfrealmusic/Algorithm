import math

# 入力
ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())

# ベクトル BA, BC, CA, CB の成分表示を求める
BAx, BAy = ax - bx, ay - by
BCx, BCy = cx - bx, cy - by
CAx, CAy = ax - cx, ay - cy
CBx, CBy = bx - cx, by - cy

# どのパターンに当てはまるか判定する
pattern = 2
if BAx * BCx + BAy * BCy < 0:
	pattern = 1
if CAx * CBx + CAy * CBy < 0:
	pattern = 3

# 点と直線の距離を求める
if pattern == 1:
	answer = math.sqrt(BAx ** 2 + BAy ** 2)
if pattern == 3:
	answer = math.sqrt(CAx ** 2 + CAy ** 2)
if pattern == 2:
	S = abs(BAx * BCy - BAy * BCx)
	BCLength = math.sqrt(BCx ** 2 + BCy ** 2)
	answer = S / BCLength

# 答えの出力
print("%.12f" % answer)

# 入力
N = int(input())
x = [0 for i in range(N)]
y = [0 for i in range(N)]
for i in range(N):
	x[i],y[i] = map(int, input().split())

# 全探索
Answer = 1000000000.0
for i in range(N):
	for j in range(i+1,N):
		dist = (((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5)
		Answer = min(Answer, dist)

# 答えの出力
print("%.12f" % Answer)

import math

# 入力
A, B, H, M = map(float, input().split())

# 座標を求める
PI = 3.14159265358979
AngleH = 30.0 * H + 0.5 * M
AngleM = 6.0 * M
Hx = A * math.cos(AngleH * PI / 180.0)
Hy = A * math.sin(AngleH * PI / 180.0)
Mx = B * math.cos(AngleM * PI / 180.0)
My = B * math.sin(AngleM * PI / 180.0)

# 答えを出力
d = (((Hx - Mx) ** 2 + (Hy - My) ** 2) ** 0.5)
print("%.12f" % d)