"""
題號：syc_703
題名：早餐店點單
描述：
早餐店依序收到顧客點的餐點名稱（英文單字），每行一個，輸入 end 表示結束（end 不列入資料），至少有 3 筆。 請將餐點存入數組，依序輸出：
1.  整個數組
2.  前三筆餐點組成的數組
3.  最後三筆餐點組成的數組
"""

# 解答
orders = ()
while True:
    item = input().strip()
    if item == "end":
        break
    orders += (item,)
print(orders)
print(orders[:3])
print(orders[-3:])
