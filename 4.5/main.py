import sys

# 深さ優先探索を行う関数
def dfs(pos, G, visited):
	visited[pos] = True
	for i in G[pos]:
		if visited[i] == False:
			dfs(i, G, visited)

# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(120000)

# 入力
N, M = map(int, input().split())
A = [ None ] * M
B = [ None ] * M
for i in range(M):
	A[i], B[i] = map(int, input().split())

# 隣接リストの作成
G = [ list() for i in range(N + 1) ]
for i in range(M):
	G[A[i]].append(B[i])
	G[B[i]].append(A[i])

# 深さ優先探索
visited = [ False ] * (N + 1)
dfs(1, G, visited)

# 連結かどうかの判定（answer = true のとき連結）
answer = True
for i in range(1, N + 1):
	if visited[i] == False:
		answer = False
if answer == True:
	print("The graph is connected.")
else:
	print("The graph is not connected.")
 
 # 入力
N, M = map(int, input().split())
A = [ None ] * M
B = [ None ] * M
for i in range(M):
	A[i], B[i] = map(int, input().split())

# 隣接リストの作成
G = [ list() for i in range(N + 1) ] # G[i] は頂点 i に隣接する頂点のリスト
for i in range(M):
	G[A[i]].append(B[i]) # 頂点 A[i] に隣接する頂点として B[i] を追加
	G[B[i]].append(A[i]) # 頂点 B[i] に隣接する頂点として A[i] を追加

# 出力（len(G[i]) は頂点 i に隣接する頂点のリストの大きさ ＝ 次数）
for i in range(1, N + 1):
	output = str(i) + ": {"
	for j in range(len(G[i])):
		if j >= 1:
			output += ","
		output += str(G[i][j]) # G[i][j] は頂点 i に隣接する頂点のうち j+1 番目のもの
	output += "}"
	print(output)
 
import queue

# 入力
N, M = map(int, input().split())
A = [ None ] * M
B = [ None ] * M
for i in range(M):
	A[i], B[i] = map(int, input().split())

# 隣接リストの作成
G = [ list() for i in range(N + 1) ]
for i in range(M):
	G[A[i]].append(B[i])
	G[B[i]].append(A[i])

# 幅優先探索の初期化 (dist[i] = -1 のとき、未到達の白色頂点である）
dist = [ -1 ] * (N + 1)
Q = queue.Queue()
dist[1] = 0
Q.put(1) # Q に 1 を追加（操作 1）

# 幅優先探索
while not Q.empty():
	pos = Q.get() # Q の先頭を調べ、これを取り出す（操作 2, 3）
	for nex in G[pos]:
		if dist[nex] == -1:
			dist[nex] = dist[pos] + 1
			Q.put(nex) # Q に nex を追加（操作 1）

# 頂点 1 から各頂点までの最短距離を出力
for i in range(1, N + 1):
	print(dist[i])
 
 # 入力
N, M = map(int, input().split())
A = [ None ] * M
B = [ None ] * M
for i in range(M):
	A[i], B[i] = map(int, input().split())

# 隣接リストの作成
G = [ list() for i in range(N + 1) ]
for i in range(M):
	G[A[i]].append(B[i])
	G[B[i]].append(A[i])

# 答えを求める
answer = 0
for i in range(1, N + 1):
	cnt = 0
	for j in G[i]:
		if j < i:
			cnt += 1
	# 自分自身より番号が小さい隣接頂点が 1 つであれば answer に 1 を加算する
	if cnt == 1:
		answer += 1

# 答えを出力
print(answer)

# このプログラムは、c[i-1][j-1] がマス (i, j) を指すように実装しています。
# マス (i, j) の頂点番号は i * W + j とすると、頂点番号 0, 1, 2, ..., HW-1 の頂点が 1 個ずつになります。

import queue

# 入力
H, W = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())
c = [ input() for i in range(H) ]
start = (sx - 1) * W + (sy - 1)
goal = (gx - 1) * W + (gy - 1)

# 隣接リストの作成
G = [ list() for i in range(H * W) ]

# 横方向の辺 [(i, j) - (i, j+1)] をグラフに追加
for i in range(H):
	for j in range(W - 1):
		if c[i][j] == "." and c[i][j + 1] == ".":
			idx1 = i * W + j  # マス (i, j) の頂点番号
			idx2 = i * W + (j + 1)  # マス (i, j + 1) の頂点番号
			G[idx1].append(idx2)
			G[idx2].append(idx1)

# 縦方向の辺 [(i, j) - (i+1, j)] をグラフに追加
for i in range(H - 1):
	for j in range(W):
		if c[i][j] == "." and c[i + 1][j] == ".":
			idx1 = i * W + j  # マス (i, j) の頂点番号
			idx2 = (i + 1) * W + j  # マス (i + 1, j) の頂点番号
			G[idx1].append(idx2)
			G[idx2].append(idx1)

# 幅優先探索の初期化 (dist[i] = -1 のとき、未到達の白色頂点である）
dist = [ -1 ] * (H * W)
Q = queue.Queue()
dist[start] = 0
Q.put(start) # Q に start を追加

# 幅優先探索
while not Q.empty():
	pos = Q.get() # Q の先頭を調べ、これを取り出す
	for nex in G[pos]:
		if dist[nex] == -1:
			dist[nex] = dist[pos] + 1
			Q.put(nex) # Q に nex を追加

# 答えを出力
print(dist[goal])

import heapq

# 入力
K = int(input())

# 隣接リストの作成 → グラフの辺を追加
G = [ list() for i in range(K) ]
for i in range(K):
	for j in range(10):
		if i == 0 and j == 0:
			continue
		G[i].append(((i * 10 + j) % K, j))

# ダイクストラ法：配列の初期化など
dist = [ 10 ** 10 ] * K
used = [ False ] * K
Q = list()
heapq.heappush(Q, (0, 0))  # ここでは dist[0] = 0 にはしないことに注意！

# ダイクストラ法：優先度付きキューの更新
while len(Q) >= 1:
	pos = heapq.heappop(Q)[1]
	if used[pos] == True:
		continue
	used[pos] = True
	for i in G[pos]:
		to = i[0]
		cost = dist[pos] + i[1]
		if pos == 0:
			cost = i[1]  # 頂点 0 の場合は例外
		if dist[to] > cost:
			dist[to] = cost
			heapq.heappush(Q, (dist[to], to))

# 答えを出力
print(dist[0])