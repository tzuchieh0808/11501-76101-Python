"""
題號：syc_704
題名：刪除重複資料
描述：
第一行輸入資料筆數 n（n ≥ 1），接下來 n 行各一個整數（可能為負數、可能重複）。 請刪除重複項目，依序輸出兩行串列：
1.  依照第一次出現的順序排列的不重複資料
2.  由小到大排列的不重複資料
"""

# 解答
n = int(input())
seen = set()
order = []
for i in range(n):
    x = int(input())
    if x not in seen:
        seen.add(x)
        order.append(x)
print(order)
print(sorted(seen))
