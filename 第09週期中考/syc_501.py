"""
題號：syc_501
題名：票價計算
描述：
請撰寫函式 price(age)，依年齡回傳票價：未滿 6 歲 0 元、6–11 歲 50 元、12–64 歲 100 元、65 歲以上 50 元。在 main() 中輸入年齡並輸出票價。
"""

# 解答
def price(age):
    if age < 6:
        return 0
    elif age < 12:
        return 50
    elif age < 65:
        return 100
    else:
        return 50

def main():
    age = int(input())
    print("Age", age, "ticket price:", price(age))

main()
