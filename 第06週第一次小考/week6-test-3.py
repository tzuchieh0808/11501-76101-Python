"""
題號：week6-test-3
題名：英鎊盎司轉公斤
描述：
請輸入英鎊(pound)及盎司(ounce)，計算出對應的公斤(kilogram)為何(小數點後8位)。
轉換參考：1英鎊(pound) = 16盎司(ounce)，1英鎊(pound) = 453.59237公克(gram)，1公斤(kilogram)=1000公克(gram)
"""

# 解答
pound = int(input())
ounce = int(input())

total_pound = pound + (ounce / 16)
total_gram = total_pound * 453.59237
total_kg = total_gram / 1000

print("%d POUND + %d OUNCE = %.8f KG" % (pound, ounce, total_kg))
