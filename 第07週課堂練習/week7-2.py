"""
題號：week7-2
題名：絕對值函式
描述：
請使用函式方法撰寫作業，在main()函式中呼叫一個計算絕對值的函式 (例:  absolute(x))，並輸入一些數值測試。
"""

# 解答
def absolute(x):
    if x < 0:
        return -x
    else:
        return x

def main():
    x = int(input("Please enter a integer number: "))
    print("The absolute value of %d is %d" %(x, absolute(x)))

main()
