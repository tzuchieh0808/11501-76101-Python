"""
題號：H0911
題名：比N小的奇數
描述：
輸入一個整數N，輸出比N小的奇數。
"""

# 解答
N=int(input())
for k in range(1,N,2):
  print(k)
