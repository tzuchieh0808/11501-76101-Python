"""
題號：PY-2020
題名：判斷奇偶
描述：
從鍵盤讀入1個整數，判斷是否為偶數，如果是則顯示EVEN，如果不是則顯示ODD。
"""

# 解答
num = int(input())
if( num%2 == 0 ):
    print("EVEN")
else:
    print("ODD")
