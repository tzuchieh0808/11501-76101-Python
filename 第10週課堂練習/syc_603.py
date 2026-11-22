"""
題號：syc_603
題名：一週步數紀錄
描述：
輸入連續 n 天（3～14 天）的步數：第一行為筆數 n，接下來 n 行每行一個整數。分三行輸出（直接 print 串列）：
1. 最近 3 天的步數
2. 第 1、3、5…天（隔天）的步數
3. 去掉第一天和最後一天後的步數
"""

# 解答
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
print(lst[-3:])
print(lst[::2])
print(lst[1:-1])
