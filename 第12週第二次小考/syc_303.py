"""
題號：syc_303
題名：兩數之間的閏年個數
描述：
從鍵盤讀入 2 個西元年份 A、B（正整數，分兩行輸入，保證 A ≤ B），計算 A 年到 B 年（含頭尾）之間共有幾個閏年。（閏年的年份必須為 4 的倍數，但不得為 100 的倍數，但可以是 400 的倍數）
"""

# 解答
a = int(input())
b = int(input())
count = 0
for i in range(a, b + 1):
    if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
        count = count + 1
print(count)
