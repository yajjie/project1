import pandas as pd
import numpy as np

# 1. 先用 list 建立 stock1
# 提示：範例輸出中的型態為 float64，因此在這裡指定 dtype=float 讓 None 自動轉為 NaN
stock1 = pd.Series([120, 80, None, 60, 95, None, 110], dtype=float)

# 2. 再加入索引 Apple, Banana, Orange, Mango, Grape, Peach, Melon 建立 stock2
index_labels = ['Apple', 'Banana', 'Orange', 'Mango', 'Grape', 'Peach', 'Melon']
stock2 = pd.Series([120, 80, None, 60, 95, None, 110], index=index_labels, dtype=float)

# 3. 接著將 stock2 轉為字典 stock3
stock3 = stock2.to_dict()

# 4. 最後依範例格式輸出各項結果
print("stock1")
print(stock1)
print()

print("stock2")
print(stock2)
print()

print("stock3")
print(stock3)
print()

# 輸出 Banana 的庫存值
print(f"Banana 庫存 : {stock2['Banana']}\n")

# 計算與檢查缺失值
print("缺失值檢查 :")
missing_check = stock2.isnull()
print(missing_check)
print()

print(f"缺失值數量 : {missing_check.sum()}")

# 5. 把 stock2 存檔為 0520_stock.csv
stock2.to_csv('0520_stock.csv', header=False)