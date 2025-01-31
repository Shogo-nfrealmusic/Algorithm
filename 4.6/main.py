N = int(input())

a = [ None ] * (N + 1)
a[1], a[2] = 1, 1
for i in range(3, N + 1):
	a[i] = a[i - 1] + a[i - 2]

print(a[N] % 1000000007)

# このプログラムを N = 1000 で実行すると、正しく 517691607 と出力されます。
# しかし、大きな数の計算を行うのに時間がかかるので、N = 100000 程度でも実行に 1 秒ほどかかります。


N = int(input())

a = [ None ] * (N + 1)
a[1], a[2] = 1, 1
for i in range(3, N + 1):
	a[i] = (a[i - 1] + a[i - 2]) % 1000000007

print(a[N] % 1000000007)

# このプログラムは、N = 100000 でも 0.05 秒ほどの実行で答えが求まります。
# これは、コード 4.6.1 と比較して数十倍速いスピードです。
# N <= 10 ** 7 の制約では実行に最大 3 秒ほどかかってしまいますが、PyPy3 で実行すれば 1 秒の制限に間に合います。


# 繰り返し二乗法（p は a**1, a**2, a**4, a**8, ... といった値をとる）
def modpow(a, b, m):
	p = a
	answer = 1
	for i in range(30):
		if (b & (1 << i)) != 0:
			answer = (answer * p) % m
		p = (p * p) % m
	return answer

MOD = 1000000007

a, b = map(int, input().split())
print(modpow(a, b, MOD))

# 補足
# 実は、Python では「a**b を m で割った余り」を繰り返し二乗法で求める関数 pow(a, b, m) が標準ライブラリとして使えます。
# Code_4_06_4_extra.py はこれを使ったプログラムです。こちらもぜひ見てください。

# 繰り返し二乗法（p は a**1, a**2, a**4, a**8, ... といった値をとる）
def modpow(a, b, m):
	p = a
	answer = 1
	for i in range(30):
		if (b & (1 << i)) != 0:
			answer = (answer * p) % m
		p = (p * p) % m
	return answer

# division(a, b, m) は a÷b mod m を返す関数
def division(a, b, m):
	return (a * modpow(b, m - 2, m)) % m

MOD = 1000000007

# 入力
X, Y = map(int, input().split())

# 二項係数の分子と分母を求める（手順 1.／手順 2.）
bunshi, bunbo = 1, 1
for i in range(1, X + Y + 1):
	bunshi = (bunshi * i) % MOD
for i in range(1, X + 1):
	bunbo = (bunbo * i) % MOD
for i in range(1, Y + 1):
	bunbo = (bunbo * i) % MOD

# 答えを求める（手順 3.）
print(division(bunshi, bunbo, MOD))

# 繰り返し二乗法（p は a**1, a**2, a**4, a**8, ... といった値をとる）
def modpow(a, b, m):
	p = a
	answer = 1
	for i in range(30):
		if (b & (1 << i)) != 0:
			answer = (answer * p) % m
		p = (p * p) % m
	return answer

# division(a, b, m) は a÷b mod m を返す関数
def division(a, b, m):
	return (a * modpow(b, m - 2, m)) % m

# 入力
X, Y = map(int, input().split())
mod = 1000000007

# 場合分け（a, b が負になってしまう場合）
if (2 * Y - X) < 0 or (2 * X - Y) < 0:
	print(0)

# 場合分け（a, b が整数にならない場合）
elif (2 * Y - X) % 3 != 0 or (2 * X - Y) % 3 != 0:
	print(0)

# 答えがゼロではないケースの場合
else:
	bunshi = 1
	bunbo = 1
	a = (2 * Y - X) // 3
	b = (2 * X - Y) // 3
	
	# 二項係数の分母と分子を求める（手順 1. / 手順 2.）
	for i in range(1, a + b + 1):
		bunshi *= i
		bunshi %= mod
	for i in range(1, a + 1):
		bunbo *= i
		bunbo %= mod
	for i in range(1, b + 1):
		bunbo *= i
		bunbo %= mod
	
	# 答えを求める（手順 3.）
	print(division(bunshi, bunbo, mod))
 
 
 # 繰り返し二乗法（p は a**1, a**2, a**4, a**8, ... といった値をとる）
def modpow(a, b, m):
	p = a
	answer = 1
	for i in range(60):
		if (b & (1 << i)) != 0:
			answer = (answer * p) % m
		p = (p * p) % m
	return answer

# division(a, b, m) は a÷b mod m を返す関数
def division(a, b, m):
	return (a * modpow(b, m - 2, m)) % m

# 入力
MOD = 1000000007
N = int(input())

# 答えの計算
V = modpow(4, N + 1, MOD) - 1
Answer = division(V, 3, MOD)

# 出力
print(Answer)