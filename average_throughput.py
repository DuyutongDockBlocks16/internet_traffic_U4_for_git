import pandas as pd

df = pd.read_csv('result.csv')

df['Length'] = pd.to_numeric(df['Length'], errors='coerce')

total_time = df['Time'].max() - df['Time'].min()

total_length = df['Length'].sum()

average_throughput = total_length / total_time

print(f'Average Throughput: {average_throughput} bytes per second')