"""
題號：PY-3051
題名：上一個閏年
描述：
從鍵盤讀入1個西元年份(正整數)，找出前一個閏年的年份。
"""

# 解答
num = int(input())-1
while(1):
    if(num%4==0):
        if(num%100==0):
            if(num%400==0):
                print(num)
                break
        else:
            print(num)
            break
    num = num-1
