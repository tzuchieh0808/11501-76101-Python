"""
題號：H0702
題名：舉重比賽
描述：
輸入年齡與體重，年齡必須大於等於15且體重必須大於等於40才能參加舉重比賽。
"""

# 解答
age=int(input("Age:\n"))
weight=int(input("Weight:\n"))
if age>=15 and weight>=40:
  print("Yes")
else:
  print("No")
