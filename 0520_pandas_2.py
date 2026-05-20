import pandas as pd

# 題目：請使用 pandas 建立一份商品銷售資料（欄位：商品名稱、價格、與銷售量）
products = ['Apple', 'Banana', 'Orange', 'Mango', 'Grape', 'Guava']
prices = [30, 20, 25, 60, 45, 35]
sales = [100, 150, 80, 60, 90, 54]

print("=== 1. 建立 DataFrame ===")
# 方式一：使用「字典 (Dictionary)」建立 DataFrame
data_dict = {
    'Product': products,
    'Price': prices,
    'Sales': sales
}
df_from_dict = pd.DataFrame(data_dict)
print("【字典建立結果】")
print(df_from_dict)
print()

# 方式二：使用「列表 (List of Lists)」建立 DataFrame
data_list = [
    ['Apple', 30, 100],
    ['Banana', 20, 150],
    ['Orange', 25, 80],
    ['Mango', 60, 60],
    ['Grape', 45, 90],
    ['Guava', 35, 54]
]
df_from_list = pd.DataFrame(data_list, columns=['Product', 'Price', 'Sales'])
print("【列表建立結果】")
print(df_from_list)
print("\n" + "="*30 + "\n")

# 後續操作使用 df 作為對象
df = df_from_dict

# 2. 觀察資料的前 5 筆與後 5 筆內容
print("=== 2. 前 5 筆與後 5 筆內容 ===")
print("【前 5 筆 (head)】")
print(df.head(5))
print("\n【後 5 筆 (tail)】")
print(df.tail(5))
print("\n" + "="*30 + "\n")

# 3. 回傳資料的列數與欄數 (Shape)
print("=== 3. 資料的列數與欄數 ===")
print(f"列數與欄數 (shape): {df.shape}")
print("\n" + "="*30 + "\n")

# 4. 欄位名稱 (Columns)
print("=== 4. 欄位名稱 ===")
print(f"欄位名稱 (columns): {df.columns}")
print("\n" + "="*30 + "\n")

# 5. 顯示資料型態 (Data Types)
print("=== 5. 資料型態 ===")
print(df.dtypes)
print("\n" + "="*30 + "\n")

# 6. 非空值數量 (Non-Null Count)
print("=== 6. 非空值數量 ===")
print(df.count())
print("\n" + "="*30 + "\n")

# 7. 計算數值欄位的統計資訊（皆取小數後 2 位）
print("=== 7. 描述性統計資訊 ===")
# 使用 .describe() 計算平均、標準差、最大值、最小值與四分位數，再配合 .round(2) 取小數後兩位
summary_stats = df.describe().round(2)
print(summary_stats)
print("\n" + "="*30 + "\n")

# 8. 把統計資訊存檔為 0520_stock2.csv
summary_stats.to_csv('0520_stock2.csv')
print("已成功將統計資訊存檔至 '0520_stock2.csv'")