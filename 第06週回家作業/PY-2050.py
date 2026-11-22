"""
題號：PY-2050
題名：最小公倍數
描述：
從鍵盤讀入2個正整數，找出其最小公倍數。
"""

# 解答
num1 = int(input())
num2 = int(input())
if(num1>num2):
    ans = num1
else:
    ans = num2
    
while(1):
    if(ans%num1==0):
        if(ans%num2==0):
            break
    ans = ans+1
print("LCM(", num1, ",", num2, ")=",ans, sep="")
