"""
題號：syc_304
題名：比N小的偶數總和
描述：
輸入一個正整數 N，計算所有比 N 小的正偶數總和並輸出。
"""

# 解答
n = int(input())
total = 0
for i in range(2, n, 2):
    total = total + i
print(total)
