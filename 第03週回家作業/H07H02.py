"""
題號：H07H02
題名：氣溫語錄
描述：
輸入攝氏溫度，大於33時，請輸出"So hot!"，否則大於30時，請輸出"Hot!"，否則大於15時，請輸出"Good!"，否則請輸出"Cold!"。
"""

# 解答
C=int(input())
if C>33:
	print("So hot!")
elif C>30:
	print("Hot!")
elif C>15:
	print("Good!")
else:
	print("Cold!")
