"""
題號：syc_701
題名：一週氣溫紀錄
描述：
氣象站每天記錄一次整數氣溫（單位 °C）。請讀入數個整數氣溫，每行一個，輸入 -9999 表示結束（-9999 不列入資料），至少有 1 筆資料。 請將資料存入數組，依序輸出：
1.  整個數組
2.  Length: 資料筆數
3.  Max: 最高溫
4.  Min: 最低溫
5.  Sum: 總和
"""

# 解答
temps = ()
while True:
    t = int(input())
    if t == -9999:
        break
    temps += (t,)
print(temps)
print("Length:", len(temps))
print("Max:", max(temps))
print("Min:", min(temps))
print("Sum:", sum(temps))
