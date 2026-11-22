"""
題號：PY-2033
題名：判斷閏年
描述：
從鍵盤讀入1個西元年份，判斷該年是否為閏年。
(閏年的年份必須為4的倍數，但不得為100的倍數，但可以是400的倍數)
"""

# 解答
year = int(input())
if( year%4 == 0 ):
    if( year%100 == 0 ):
        if( year%400 == 0 ):
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
else:
    print("NO")
