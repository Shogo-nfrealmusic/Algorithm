# def isprime(N):
# 	for i in range(2, N):
# 		if N % i == 0:
# 			return False # N が i で割り切れた場合、この時点で素数ではないと分かる
# 	return True

# N = int(input())
# if isprime(N):
# 	print("prime")
# else:
# 	print("not prime")
 
 # 2 以上の整数 N に対し、N が素数であれば true、素数でなければ false を返す関数
# def isprime(N):
# 	LIMIT = int(N ** 0.5)
# 	for i in range(2, LIMIT + 1):
# 		if N % i == 0:
# 			return False
# 	return True

# N = int(input())
# if isprime(N):
# 	print("prime")
# else:
# 	print("not prime")
 
 # このプログラムは、コード 3.1.3 とは異なり、約数を小さい順に出力するプログラムとなっています。

# # 入力
# N = int(input())

# # すべての約数を求め、配列 divisors に入れる
# LIMIT = int(N ** 0.5)
# divisors = []
# for i in range(1, LIMIT + 1):
# 	if N % i == 0:
# 		divisors.append(i)
# 		if i != N // i:
# 			divisors.append(N // i)

# # 小さい順に並べ替え → 出力
# # sort は小さい順に並べ替える関数です（3.6.1 項で扱います）
# divisors.sort()
# for i in divisors:
# 	print(i)

def prime_factorization(N):
    factors = []  # 素因数を格納するリスト
    LIMIT = int(N ** 0.5)  # √Nまで調べる

    # 2で割れる限り割る
    while N % 2 == 0:
        factors.append(2)
        N //= 2

    # 奇数で割れるか試す
    for i in range(3, LIMIT + 1, 2):  # 3から√Nまでの奇数
        while N % i == 0:  # 割り切れる限り割る
            factors.append(i)
            N //= i

    # 最後に残った数が素数の場合
    if N > 2:
        factors.append(N)

    return factors

# 入力と出力
N = int(input("自然数を入力してください: "))
factors = prime_factorization(N)
print(f"{N} の素因数分解結果: {factors}")
