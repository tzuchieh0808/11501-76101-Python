"""
題號：syc_607
題名：三位學生成績單
描述：
輸入 12 行，每行一個整數，依序為 3 位學生各 4 科成績（第 1 位的 4 科、第 2 位的 4 科…）。請存成 3×4 的二維串列後：
前三行各輸出一位學生的「總分 平均」（平均取到小數點後 2 位）；第四行輸出各科最高分（4 個數，空白隔開）。
"""

# 解答
score = []
for i in range(3):
    row = []
    for j in range(4):
        row.append(int(input()))
    score.append(row)
for i in range(3):
    total = sum(score[i])
    print(total, "%.2f" % (total / 4))
top = []
for j in range(4):
    best = score[0][j]
    for i in range(1, 3):
        if score[i][j] > best:
            best = score[i][j]
    top.append(best)
print(top[0], top[1], top[2], top[3])
