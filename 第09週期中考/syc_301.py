"""
題號：syc_301
題名：閏年個數
描述：
從鍵盤讀入 1 個西元年份 Y（正整數），計算西元 1 年到 Y 年（含）之間共有幾個閏年。
（閏年的年份必須為4的倍數，但不得為100的倍數，但可以是400的倍數）
"""

# 解答
y = int(input())
count = 0
for i in range(1, y + 1):
    if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
        count = count + 1
print(count)
