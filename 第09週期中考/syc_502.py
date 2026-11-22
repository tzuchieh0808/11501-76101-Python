"""
題號：syc_502
題名：2 的 n 次方
描述：
請撰寫函式 power2(n)，在函式內用 for 迴圈計算 2 的 n 次方並回傳（不可使用 ** 或 pow）。在 main() 中輸入 0–40 的整數並輸出。
"""

# 解答
def power2(n):
    result = 1
    for i in range(n):
        result = result * 2
    return result

def main():
    n = int(input())
    print("2 ^", n, "=", power2(n))

main()
