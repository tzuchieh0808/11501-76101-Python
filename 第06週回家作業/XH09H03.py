"""
題號：XH09H03
題名：不斷NM乘法表
描述：
輸入N與M，印出NX1到NXM，當N=0時結束。
"""

# 解答
while 1:
  N=int(input())
  if N==0:
    break
  M=int(input())
  for k in range(1,M+1):
    print(N,"X",k,"=",N*k)
