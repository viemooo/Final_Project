import pandas as pd
import matplotlib.pyplot as plt

# 示例数据（用你自己的数据替换）
data = {
    'Date': ['2023-07-01', '2023-07-02', '2023-07-03', '2023-07-04', '2023-07-05'],
    'TimeSeries1': [10, 15, 20, 25, 30],
    'TimeSeries2': [5, 12, 18, 22, 28],
    'OtherVariable': [50, 60, 70, 80, 90]
}

df = pd.DataFrame(data)

# 将日期列转换为日期时间格式
df['Date'] = pd.to_datetime(df['Date'])

# 创建画布和子图
fig, ax = plt.subplots()

# 绘制第一个时间序列的线图
ax.plot(df['Date'], df['TimeSeries1'], label='Time Series 1', marker='o')

# 绘制第二个时间序列的线图
ax.plot(df['Date'], df['TimeSeries2'], label='Time Series 2', marker='o')

# 绘制其他变量的线图
ax.plot(df['Date'], df['OtherVariable'], label='Other Variable', marker='o')

# 添加标签和标题
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Two Time Series and Other Variable Line Chart')

# 添加图例
plt.legend()

# 旋转x轴刻度，使得日期标签更清晰可读
plt.xticks(rotation=45)

# 展示图形
plt.show()
