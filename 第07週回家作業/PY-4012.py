"""
題號：PY-4012
題名：攝氏轉華氏
描述：
從鍵盤讀入攝氏溫度，將攝氏溫度轉換為華氏溫度，計算至小數後兩位四捨五入，並將結果顯示在畫面上。
(華氏溫度 = 攝氏溫度*(9/5)+32)
"""

# 解答
celsius = float(input())
fahrenheit = celsius*(9/5)+32
celsius = round(celsius, 2)
fahrenheit = round(fahrenheit, 2)
print("%.2fC = %.2fF" %(celsius,fahrenheit))
