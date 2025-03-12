N = int(input())
T = list(map(int, input().split()))

sumT = sum(T)
dp = [[False] * (sumT + 1) for i in range(N + 1)]
dp[0][0] = True

for i in range(1, N+1):
    for j in range(sumT + 1):
        if j < T[i-1]:
            if dp[i-1][j] == True:
                dp[i][j] == True
            else:
                dp[i][j] == False
        if j >= T[i - 1]:
            if dp[i - 1][j] == True or dp[i - 1][j - T[i - 1]] == True:
                dp[i][j] = True
            else:
                dp[i][j] = False

answer = 10 ** 10  # 仮の最小値として大きな値を設定
for i in range(sumT + 1):  # 0分 〜 sumT分 まで全て試す
    if dp[N][i] == True:  # `N` 個の料理を使って `i` 分が作れるか？
        cooking_time = max(i, sumT - i)  # 2つのオーブンの最大時間を計算
        answer = min(answer, cooking_time)  # 最小の調理時間を更新
print(answer)  # 最小の最大時間を出力
