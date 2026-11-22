"""
題號：syc_602
題名：排隊叫號
描述：
輸入排隊民眾的號碼牌：第一行為筆數 n，接下來 n 行每行一個整數（n ≥ 2）。分三行輸出：第一位、最後一位、倒數第二位的號碼。（提示：可用負索引）
"""

# 解答
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
print(lst[0])
print(lst[-1])
print(lst[-2])
