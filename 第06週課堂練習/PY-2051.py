"""
題號：PY-2051
題名：最大公因數
描述：
從鍵盤讀入2個正整數，找出其最大公因數。
"""

# 解答
num1 = int(input())
num2 = int(input())
if(num1>num2):
    ans = num2
else:
    ans = num1
while(1):
    if(num1%ans==0):
        if(num2%ans==0):
            break
    ans = ans-1
print("GCD(", num1, ",", num2, ")=",ans, sep="")
