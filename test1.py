import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件，指定逗号为分隔符
csv_file_path = "result.csv"
df = pd.read_csv(csv_file_path, delimiter=',')

# 过滤掉协议是 ARP、MDNS 和 ICMP 的行
filtered_df = df[~df['Protocol'].isin(['ARP', 'MDNS', 'ICMP'])]

# 设置合适的时间间隔（例如，1秒）
interval = 1  # 1秒

# 将时间字段转换为 datetime 对象
filtered_df['Time'] = pd.to_datetime(filtered_df['Time'], errors='coerce')

# 对时间进行分组，并计算每个时间间隔的流量量和包长度的累加
grouped = (
    filtered_df.groupby(pd.Grouper(key='Time', freq=f'{interval}s'))
    .agg({'Length': 'sum', 'Time': 'count'})
    .rename(columns={'Length': 'total_length', 'Time': 'packet_count'})
    .reset_index()
)

# 计算包长度的累加
grouped['cumulative_length'] = grouped['total_length'].cumsum()

# 绘制流量量图
plt.figure(figsize=(20, 6))
plt.plot(grouped['Time'], grouped['packet_count'], marker='o', linestyle='-', label='Packet Count')
plt.plot(grouped['Time'], grouped['cumulative_length'], marker='o', linestyle='-', label='Cumulative Length', color='orange')

plt.title('Traffic Volume Over Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Count')
plt.legend()
plt.tight_layout()
plt.show()
