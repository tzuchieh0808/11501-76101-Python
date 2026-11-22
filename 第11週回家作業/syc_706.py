"""
題號：syc_706
題名：社團成員比對
描述：
A、B 兩個社團各自輸入成員學號（整數），每行一個，各以 0 結束（0 不列入資料）。社團可能沒有任何成員，同一社團的學號也可能重複輸入。 請依序輸出四行，每行為由小到大排序的串列：
1.  Union: 兩社團的所有成員
2.  Both: 同時參加兩社團的成員
3.  OnlyB: 只參加 B 社團、沒參加 A 社團的成員
4.  Either: 只參加其中一個社團的成員
"""

# 解答
a = set()
while True:
    x = int(input())
    if x == 0:
        break
    a.add(x)
b = set()
while True:
    x = int(input())
    if x == 0:
        break
    b.add(x)
print("Union:", sorted(a | b))
print("Both:", sorted(a & b))
print("OnlyB:", sorted(b - a))
print("Either:", sorted(a ^ b))
