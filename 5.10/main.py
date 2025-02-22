# import math

# a, b, c = map(int, input().split())

# if math.sqrt(a) + math.sqrt(b) < math.sqrt(c):
# 	print("Yes")
# else:
# 	print("No")
 
a, b, c = map(int, input().split())
if c - a - b < 0:
	print("No")
elif 4 * a * b < (c - a - b) * (c - a - b):
	print("Yes")
else:
	print("No")
 
 # 入力
N, X, Y = map(int, input().split())

# 4 つの整数 (a, b, c, d) の全探索
flag = False
for a in range(1, N + 1):
	for b in range(a, N + 1):
		for c in range(b, N + 1):
			for d in range(c, N + 1):
				if a + b + c + d == X and a * b * c * d == Y:
					flag = True  # 答えが見つかったら flag を true にする

# 答えの出力
if flag == True:
	print("Yes")
else:
	print("No")

# p.256 注 5.10.2 に書かれてあるように、Python は実行速度が遅いので、最大ケースでは実行に数十秒かかります。
# しかし、同じプログラムを PyPy3 で実行すると、最大ケースでも 1 秒ほどで答えを求めることができます。
# より良い計算量のプログラムについては、Code_5_10_3_extra.py を見てください。

N, X, Y = map(int, input().split())

if Y > N ** 4:
	print("No")
else:
	d = []
	for i in range(1, N + 1):
		if Y % i == 0:
			d.append(i)
	divcnt = len(d)
	flag = False
	for i in range(0, divcnt):
		for j in range(i, divcnt):
			for k in range(j, divcnt):
				for l in range(k, divcnt):
					if d[i] + d[j] + d[k] + d[l] == X and d[i] * d[j] * d[k] * d[l] == Y:
						flag = True
	if flag == True:
		print("Yes")
	else:
		print("No")

# 実は、このプログラムの計算量は O(N) です。
# この理由をぜひ考えてみましょう。


# 入力
N = int(input())
S = input()

# '(' の数 - ')' の数を depth とする
# 途中で depth が負になったら、この時点で No
depth = 0
flag = True
for i in range(N):
	if S[i] == '(':
		depth += 1
	if S[i] == ')':
		depth -= 1
	if depth < 0:
		flag = False

# 最後、depth = 0 ['(' と ')' の数が同じ] であるかも追加で判定する
if flag == True and depth == 0:
	print("Yes")
else:
	print("No")
 
 # 入力
N = int(input())

# 答えを求める
mod = 1000000007
val = N * (N + 1) // 2
print(val * val % mod)

# 入力
A, B, C = map(int, input().split())

# 計算
mod = 998244353
D = A * (A + 1) // 2
E = B * (B + 1) // 2
F = C * (C + 1) // 2

# 答えを出力
print((D * E * F) % mod)

import sys

# 入力
a, b, c = map(int, input().split())

# c = 1 のときの場合分け
if c == 1:
	print("No")
	sys.exit()

# 右辺の計算（c の b 乗）
v = 1
for i in range(b):
	v *= c
	if a < v:
		print("Yes")
		sys.exit()

# 出力（No の場合）
print("No")

# 整数 m の各桁の積を返す関数
def product(m):
	if m == 0:
		return 0
	ans = 1
	while m >= 1:
		ans *= (m % 10)
		m //= 10
	return ans

# 各桁の積の候補の集合を返す関数
def func(digit, m):
	if digit == 11:
		return {product(m)}
	
	# 次の桁を探索
	# min_value は cur の最後の桁（単調増加にするためには次の桁がそれ以上でなければならない）
	min_value = m % 10
	ret = set()
	for i in range(min_value, 10):
		r = func(digit + 1, m * 10 + i)
		for j in r:
			ret.add(j)
	return ret

# 入力
N, B = map(int, input().split())

# 各桁の積の候補を列挙
fm_cand = func(0, 0)

# m - f(m) = B になるかどうかチェック
Answer = 0
for fm in fm_cand:
	m = fm + B # 各桁の積から導かれる m の値
	prod_m = product(m) # 本来の f(m) の値
	if m - prod_m == B and m <= N:
		Answer += 1

# 出力
print(Answer)