"""
題號：syc_702
題名：取消訂單
描述：
網路商店的訂單編號存在數組中，數組不能直接刪除元素。 第一行輸入訂單數 n（n ≥ 1），接下來 n 行各一個整數訂單編號（編號可能重複），最後一行輸入要取消的是第 k 筆（1 ≤ k ≤ n，依位置計算，不是依編號）。
請依序輸出：
1.  原本的數組
2.  Removed: 被取消的訂單編號
3.  取消後的新數組
"""

# 解答
n = int(input())
orders = ()
for i in range(n):
    orders += (int(input()),)
k = int(input())
print(orders)
lst = list(orders)
removed = lst.pop(k - 1)
print("Removed:", removed)
print(tuple(lst))
