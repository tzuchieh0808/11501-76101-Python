"""
題號：syc_605
題名：數字排序
描述：
輸入 5 行，每行一個整數（可能為負）。由小到大排序後分四行輸出：排序後的串列、最小值、最大值、總和。
"""

# 解答
lst = []
for i in range(5):
    lst.append(int(input()))
lst.sort()
print(lst)
print(min(lst))
print(max(lst))
print(sum(lst))
