import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件，指定逗号为分隔符
csv_file_path = "result.csv"
df = pd.read_csv(csv_file_path, delimiter=',')


filtered_df = df[df['Protocol'].isin(['ICMP'])]
# filtered_df['Info'] = filtered_df['Info'].astype(str)
# filtered_df = filtered_df[~filtered_df['Info'].str.contains('5201')]

# 设置合适的时间间隔（例如，1秒）
interval = 1  # 1秒

# 对时间进行分组，并计算每个时间间隔的流量量
grouped_count = filtered_df.groupby(filtered_df['Time'] // interval * interval).size().reset_index(name='packet_count')
grouped_length = filtered_df.groupby(filtered_df['Time'] // interval * interval)['Length'].sum().reset_index(name='packet_length')

# 绘制流量量图
fig, ax1 = plt.subplots(figsize=(20, 6))

# Plot 'packet_count' on the primary y-axis
ax1.plot(grouped_count['Time'], grouped_count['packet_count'], marker='o', linestyle='-', label='Packet Count', color='b')
ax1.set_xlabel('Time (seconds)')
ax1.set_ylabel('Packet Count', color='b')
ax1.tick_params('y', colors='b')

# Create a secondary y-axis for 'packet_length'
ax2 = ax1.twinx()
ax2.plot(grouped_length['Time'], grouped_length['packet_length'], marker='x', linestyle='-', label='Packet Length', color='r')
ax2.set_ylabel('Packet Length', color='r')
ax2.tick_params('y', colors='r')

plt.title('Traffic Volume Over Time')
plt.legend()
plt.tight_layout()
plt.show()
