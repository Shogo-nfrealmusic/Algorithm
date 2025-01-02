# a, b = map(int, input().split()) # a と b を入力する
# print(a & b) # a AND b の値を出力する
# print(a | b) # a OR b の値を出力する
# print(a ^ b) # a XOR b の値を出力する

# import math

# print(math.sqrt(841))

# a = 13
# b = 14

# # AND演算
# result_and = a & b
# print("13 AND 14 =", result_and)

# # OR演算
# result_or = a | b
# print("13 OR 14 =", result_or)

# # XOR演算
# result_xor = a ^ b
# print("13 XOR 14 =", result_xor)

# result = 8 | 4 | 2 | 1
# print(result)  # 出力: 15


N = int(input())
A = list(map(int, input().split()))

# 答えの計算
Answer = 0
for i in range(N):
    Answer += A[i]

# 出力
print(Answer % 100)
