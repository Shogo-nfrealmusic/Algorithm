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