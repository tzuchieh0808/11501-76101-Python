"""
題號：syc_705
題名：健身房打卡
描述：
健身房記錄今天的會員打卡編號，同一位會員可能打卡多次。 請讀入數個整數會員編號，每行一個，輸入 0 表示結束（0 不列入資料），至少有 1 筆。 請利用集合統計，依序輸出：
1.  Check-ins: 總打卡次數
2.  Members: 不重複的會員人數
3.  Smallest: 最小會員編號
4.  Largest: 最大會員編號
"""

# 解答
ids = set()
total = 0
while True:
    x = int(input())
    if x == 0:
        break
    total += 1
    ids.add(x)
print("Check-ins:", total)
print("Members:", len(ids))
print("Smallest:", min(ids))
print("Largest:", max(ids))
