"""
題號：week6-test-2
題名：最少硬幣組合
描述：
假設有50元、10元和1元等3種硬幣，請讀入一個金額，並顯示等同於該金額所需的最少硬幣組合。
"""

# 解答
total = int(input())
min50 = total // 50
min10 = (total % 50) // 10
min1 = (total % 50) % 10
print(str(total) + '=50*' + str(min50) + '+10*' + str(min10) + '+1*' + str(min1))
