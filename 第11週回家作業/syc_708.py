"""
題號：syc_708
題名：商品價目查詢
描述：
超商用詞典記錄商品代碼與價格。 第一行輸入商品數 n，接下來每個商品輸入兩行：商品代碼、價格（皆為整數）。同一代碼若出現兩次，以後輸入的價格為準。 之後輸入要查詢的商品代碼，每行一個，以 0 結束（0 不查詢）。 每次查詢輸出一行：有此商品輸出 代碼: 價格，沒有則輸出 代碼: Not found。
"""

# 解答
n = int(input())
price = {}
for i in range(n):
    code = int(input())
    price[code] = int(input())
while True:
    q = int(input())
    if q == 0:
        break
    if q in price:
        print(str(q) + ":", price[q])
    else:
        print(str(q) + ": Not found")
