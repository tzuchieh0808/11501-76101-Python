"""
題號：PY-2047
題名：加速疾行 2
描述：
從鍵盤讀入1個正整數N，印出包含N個數字的數列，且這個數列從1開始，且數字間的間隔從1開始，逐次加1(即間隔 1, 2, 3, ...)。
"""

# 解答
num = int(input())
ans = 1
gap = 0
ans = ans+gap
count = 0 
while(count < num ):
    print(ans, end=' ')
    gap = gap+1
    ans = ans+gap
    count = count+1
