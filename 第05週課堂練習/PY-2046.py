"""
題號：PY-2046
題名：加速疾行
描述：
從鍵盤讀入1個正整數N，列印出從1開始且小於N的整數數列，且數字間的間隔從1開始，逐次加1(即間隔 1, 2, 3, ...)。
"""

# 解答
num = int(input())
ans = 1
gap = 0
ans = ans+gap
while(ans < num ):
    print(ans, end='  ')
    gap = gap+1
    ans = ans+gap
