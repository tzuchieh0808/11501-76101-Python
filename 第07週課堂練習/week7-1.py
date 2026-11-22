"""
題號：week7-1
題名：印出$符號與數字
描述：
請使用函式方法撰寫作業，在main()函式中呼叫兩個函式，
分別是printDollars()及number()。
其中，printDollars()顯示$符號，number()顯示1~9。
"""

# 解答
def printDollars():
    for i in range(20):
        print("$", end = "")
    print()

def number():
    for i in range(1, 10):
        print(" %d" %i, end = '')
    print()

def main():
    printDollars()
    number()
    printDollars()

main()
