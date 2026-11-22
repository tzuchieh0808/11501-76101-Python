"""
題號：PY-2048
題名：因數個數
描述：
讀入一個正整數，顯示所有該正整數因數的個數。
"""

# 解答
num = int(input())
ans = 0 
for i in range(1,num+1):
    if(num%i==0):
        ans = ans+1
print("ANS=", ans, sep="")
