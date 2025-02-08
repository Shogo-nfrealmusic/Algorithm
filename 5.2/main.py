# 注意：以下のプログラムは N >= 1 で正しく動作します。
# N = 0 では答えは「1」となるので、また別の場合分けをする必要があります。

N = int(input())
if N % 4 == 1:
	print(2)
if N % 4 == 2:
	print(4)
if N % 4 == 3:
	print(8)
if N % 4 == 0:
	print(6)
 
 N = int(input())
if N % 4 == 0:
	print("Second")
else:
	print("First")
 
 # 入力
N = int(input())
 
# N = 2^k-1 の形で表せるかどうかを調べる
flag = False
for i in range(1, 60):
	if N == (2 ** i) - 1:
		flag = True
 
if flag == True:
	print("Second")
else:
	print("First")
 
 import sys

# 入力
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 配列の初期化
First = [-1 for i in range(N+1)]
Second = [-1 for i in range(N+1)]

# 答えを求める
# cur は現在いる町の番号
cnt = 0
cur = 1
while True:
	# First, Second の更新
	if First[cur] == -1:
		First[cur] = cnt
	elif Second[cur] == -1:
		Second[cur] = cnt
	
	# K 回の移動後に町 cur にいるか判定
	if cnt == K:
		print(cur)
		sys.exit()
	elif Second[cur] != -1 and (K - First[cur]) % (Second[cur] - First[cur]) == 0:
		print(cur)
		sys.exit()
	
	cur = A[cur - 1]
	cnt += 1