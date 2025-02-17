N = int(input())

answer = 0

# 10000 円以上の間、10000 円札を使い続ける
while N >= 10000:
	N -= 10000
	answer += 1

# 5000 円以上の間、5000 円札を使い続ける
while N >= 5000:
	N -= 5000
	answer += 1

# 残った金額を 1000 円札で支払う
while N >= 1:
	N -= 1000
	answer += 1

print(answer)


# 入力
N = int(input())
L = [ None ] * N
R = [ None ] * N
for i in range(N):
	L[i], R[i] = map(int, input().split())

# 映画の選び方のシミュレーション
# 見れる映画の終了時刻の最小値 min_endtime は、最初 1000000 (INF で設定）のようなあり得ない値にセットする
INF = 1000000
current_time = 0  # current_time は現在時刻（直前に見た映画の終了時刻）
answer = 0
while True:
	min_endtime = INF
	for i in range(N):
		if L[i] >= current_time:
			min_endtime = min(min_endtime, R[i])
	if min_endtime == INF:
		break
	current_time = min_endtime
	answer += 1

# 答えの出力
print(answer)

# 入力
N = int(input())
Answer = 0

# 10000 円札を支払う
Answer += (N // 10000)
N %= 10000

# 5000 円札を支払う
Answer += (N // 5000)
N %= 5000

# 1000 円札を支払う
Answer += (N // 1000)
N %= 1000

# 出力
print(Answer)

# 入力
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 配列 A, B をソートする
A.sort()
B.sort()

# 答えを求める
Answer = 0
for i in range(N):
	Answer += abs(A[i] - B[i])

# 出力
print(Answer)

# 入力
# A は (終了時刻, 開始時刻) になっていることに注意 [終了時刻の昇順にソートするため]
N = int(input())
A = []
for i in range(N):
	a, b = map(int, input().split())
	A.append([b, a])

# ソート
A.sort()

# 終了時刻が最も早いものを選び続ける
CurrentTime = 0
Answer = 0
for i in range(N):
	if CurrentTime <= A[i][1]:
		CurrentTime = A[i][0]
		Answer += 1

# 出力
print(Answer)