"""
題號：PY-2049
題名：正整數因數
描述：
讀入一個正整數，找出該正整數的所有因數，並依序顯示在畫面上。
"""

# 解答
num = int(input())
print("ANS=", end="")
for i in range(1, num+1):
    if(num%i==0):
        print(i, end=" ")
