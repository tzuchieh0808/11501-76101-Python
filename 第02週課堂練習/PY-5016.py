"""
題號：PY-5016
題名：正逆數字和 2
描述：
從鍵盤讀入1個11-99且非10的倍數的整數，把所讀入數字順序翻轉後，與原數字相加，並將結果顯示在畫面上。
"""

# 解答
num = int(input())
ones = num/10
tens = num%10
print(num, "+", int(ones+tens*10), "=", int(ones+tens*10)+num, sep="")
