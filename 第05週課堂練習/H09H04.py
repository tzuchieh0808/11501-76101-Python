"""
題號：H09H04
題名：NM乘法表
描述：
輸入N與M，輸出1~N乘以1~M的乘法表。
"""

# 解答
N=int(input())
M=int(input())
for i in range(1,N+1):
  for j in range(1,M+1):
    print(i,"x",j,"=",i*j)
