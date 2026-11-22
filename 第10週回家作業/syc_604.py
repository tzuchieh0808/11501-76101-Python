"""
題號：syc_604
題名：回文號碼檢查
描述：
第一行為筆數 n，接下來 n 行每行一個整數。若此串列正著讀與反著讀相同（回文）輸出 Yes，否則輸出 No。
"""

# 解答
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
if lst == lst[::-1]:
    print("Yes")
else:
    print("No")
