"""
題號：PY-1064
題名：數轉ASCII 2
描述：
請從鍵盤讀入1個32至126的整數，並將ASCII碼為所讀入整數的字元顯示在畫面上。
請參照解答格式輸出。
"""

# 解答
ch = int(input())
print("ASCII ", ch, "=", chr(ch), sep="" )
