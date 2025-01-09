# # 正の整数 A と B の最大公約数を返す関数
# # GCD は Greatest Common Divisor（最大公約数）の略
# def GCD(A, B):
# 	answer = 0
# 	for i in range(1, min(A, B) + 1):
# 		if A % i == 0 and B % i == 0:
# 			answer = i
# 	return answer

# A, B = map(int, input().split())
# print(GCD(A, B))

# 正の整数 A と B の最大公約数を返す関数
# # GCD は Greatest Common Divisor（最大公約数）の略
# def GCD(A, B):
# 	while A >= 1 and B >= 1:
# 		if A < B:
# 			B = B % A  # A < B の場合、大きい方 B を書き換える
# 		else:
# 			A = A % B  # A >= B の場合、大きい方 A を書き換える
# 	if A >= 1:
# 		return A
# 	return B

# A, B = map(int, input().split())
# print(GCD(A, B))

# from functools import reduce

# # 2つの正の整数の最大公約数を計算する関数
# def GCD(A, B):
#     while B != 0:
#         A, B = B, A % B
#     return A

# # N個の整数の最大公約数を計算する関数
# def find_GCD_of_list(numbers):
#     # reduce関数を使ってリスト内のすべての数の最大公約数を計算
#     return reduce(GCD, numbers)

# # ユーザーから入力を受け取る
# N = int(input("Enter the number of integers (N): "))  # 整数の個数
# numbers = list(map(int, input(f"Enter {N} integers separated by space: ").split()))

# # 最大公約数を計算して出力
# result = find_GCD_of_list(numbers)
# print(f"The GCD of the given {N} integers is: {result}")

# 最大公約数を返す関数
def GCD(A, B):
	while A >= 1 and B >= 1:
		if A < B:
			B = B % A  # A < B の場合、大きい方 B を書き換える
		else:
			A = A % B  # A >= B の場合、大きい方 A を書き換える
	if A >= 1:
		return A
	return B

# 最小公倍数を返す関数
def LCM(A, B):
	return int(A / GCD(A, B)) * B

# 入力
N = int(input())
A = list(map(int, input().split()))

# 答えを求める
R = LCM(A[0], A[1])
for i in range(2, N):
	R = LCM(R, A[i])

# 出力
print(R)
