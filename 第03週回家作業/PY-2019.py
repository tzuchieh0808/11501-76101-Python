"""
題號：PY-2019
題名：判斷10倍
描述：
從鍵盤讀入1個整數，判斷是否為10的倍數，如果是則顯示YES，如果不是則顯示NO。
"""

# 解答
num = int(input())
if( num%10 == 0 ):
    print("YES")
else:
    print("NO")
