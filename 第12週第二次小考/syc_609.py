"""
題號：syc_609
題名：N個數字排序
描述：
第一行輸入正整數 N，接下來 N 行，每行一個整數（可能為負）。由小到大排序後分四行輸出：排序後的串列、最小值、最大值、總和。
"""

# 解答
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
lst.sort()
print(lst)
print(min(lst))
print(max(lst))
print(sum(lst))
