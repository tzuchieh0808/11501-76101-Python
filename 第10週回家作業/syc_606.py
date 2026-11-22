"""
題號：syc_606
題名：班上前三名
描述：
輸入 n 位同學的分數（1～10 位）：第一行為筆數 n，接下來 n 行每行一個整數。輸出由高到低的前三名分數串列；若不足 3 人就全部輸出。
"""

# 解答
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
lst.sort(reverse=True)
print(lst[:3])
