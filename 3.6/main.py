# # 入力（たとえば N = 5, A = [3, 1, 4, 1, 5] を入力したとする）
# N = int(input())
# A = list(map(int, input().split()))

# # 配列 A 全体をソートする
# A.sort()

# # 出力（1, 1, 3, 4, 5 の順に出力される）
# for i in range(N):
# 	print(A[i])
 
#  # 入力
# N = int(input())
# A = list(map(int, input().split()))

# # 選択ソート
# for i in range(N - 1):
# 	min_position = i
# 	min_value = A[i]
# 	for j in range(i + 1, N):
# 		if A[j] < min_value:
# 			min_position = j  # min_position は最小値のインデックス（0 ～ N-1）
# 			min_value = A[j]  # min_value は現時点での最小値
# 	# A[i] と A[min_position] を交換
# 	A[i], A[min_position] = A[min_position], A[i]

# # 出力
# for i in range(N):
# 	print(A[i])

# def func(N):
# 	if N == 1:
# 		return 1  # このような場合分けすべきケースを「ベースケース」といいます
# 	return func(N - 1) * N

# N = int(input())
# print(func(N))

# Python では、呼び出せる再帰関数の深さに上限が設定されており、デフォルトでは 1000 などの深さに設定されています。
# この上限は、sys.getrecursionlimit() を呼び出すことで取得できます。
# 一方、sys.setrecursionlimit(depth) を呼び出すことで、再帰呼び出しの深さ depth の上限を変えることができます。
# （これらの機能を使うためには、最初に import sys と書く必要があります）

# def GCD(A, B):
# 	if B == 0:
# 		return A  # ベースケース
# 	return GCD(B, A % B)

# A, B = map(int, input().split())
# print(GCD(A, B))

# def solve(l, r, A):
# 	if r - l == 1:
# 		return A[l]
# 	m = (l + r) // 2  # 区間 [l, r) の中央で分割する
# 	s1 = solve(l, m, A)  # s1 は A[l] + ... + A[m-1] の合計値となる
# 	s2 = solve(m, r, A)  # s2 は A[m] + ... + A[r-1] の合計値となる
# 	return s1 + s2

# # 入力
# N = int(input())
# A = list(map(int, input().split()))

# # 再帰呼び出し → 答えの出力
# answer = solve(0, N, A)
# print(answer)

def MergeSort(A):
	# 長さが 1 の場合、すでにソートされているので何もしない
	if len(A) == 1:
		return A
	
	# 2 つに分割した後、小さい配列をソート
	m = len(A) // 2
	A_Dash = MergeSort(A[0:m])
	B_Dash = MergeSort(A[m:len(A)])
	
	# この時点で以下の 2 つの配列がソートされている：
	# 列 A' に相当するもの [A_Dash[0], A_Dash[1], ..., A_Dash[m-1]]
	# 列 B' に相当するもの [B_Dash[0], B_Dash[1], ..., B_Dash[len(A)-m-1]]
	# 以下が Merge 操作となります。
	c1 = 0
	c2 = 0
	C = []
	while (c1 < len(A_Dash) or c2 < len(B_Dash)):
		if c1 == len(A_Dash):
			# 列 A' が空の場合
			C.append(B_Dash[c2])
			c2 += 1
		elif c2 == len(B_Dash):
			# 列 B' が空の場合
			C.append(A_Dash[c1])
			c1 += 1
		else:
			# そのいずれでもない場合
			if A_Dash[c1] <= B_Dash[c2]:
				C.append(A_Dash[c1])
				c1 += 1
			else:
				C.append(B_Dash[c2])
				c2 += 1
	
	# 列 A', 列 B' を合併した配列 C を返す
	return C

# 以下、メイン部分
N = int(input())
A = list(map(int, input().split()))

# マージソート → 答えの出力
Answer = MergeSort(A)
print(*Answer)