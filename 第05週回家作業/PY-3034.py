"""
題號：PY-3034
題名：等腰直角三角形
描述：
從鍵盤讀入1個正整數N(假設N<80)，在畫面上輸出高及寬均為N的星號三角形。
"""

# 解答
num = int(input())
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*", end='')
    print()
