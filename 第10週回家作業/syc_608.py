"""
題號：syc_608
題名：冷飲店冰箱存貨
描述：
冷飲店的冰箱有 2 層，每層 3 格。輸入 6 行，每行一個整數，依序為第 1 層第 1～3 格、第 2 層第 1～3 格的存貨數量。請存成 2×3 的二維串列後分四行輸出：
1. 整個二維串列（直接 print）
2. 第 2 層第 3 格的存貨
3. 第 1 層與第 2 層各自的存貨總和（空白隔開）
4. 全部存貨總和
"""

# 解答
fridge = []
for i in range(2):
    row = []
    for j in range(3):
        row.append(int(input()))
    fridge.append(row)
print(fridge)
print(fridge[1][2])
print(sum(fridge[0]), sum(fridge[1]))
print(sum(fridge[0]) + sum(fridge[1]))
