"""
題號：syc_707
題名：學號查姓名
描述：
導師用詞典記錄班上的學號與英文名字。 第一行輸入學生數 n，接下來每位學生輸入兩行：學號（整數）、英文名字（一個單字）。同一學號若出現兩次，以後輸入的名字為準。 之後輸入要查詢的學號，每行一個，以 0 結束（0 不查詢，至少查詢 1 次）。 每次查詢輸出一行：有此學號輸出 學號: 名字，沒有則輸出 學號: Unknown。
"""

# 解答
n = int(input())
names = {}
for i in range(n):
    sid = int(input())
    names[sid] = input()
while True:
    q = int(input())
    if q == 0:
        break
    if q in names:
        print(str(q) + ":", names[q])
    else:
        print(str(q) + ": Unknown")
