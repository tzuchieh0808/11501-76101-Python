"""
題號：syc_302
題名：比N小的奇數總和
描述：
輸入一個正整數 N，計算所有比 N 小的正奇數總和並輸出。
"""

# 解答
n = int(input())
total = 0
for i in range(1, n, 2):
    total = total + i
print(total)
