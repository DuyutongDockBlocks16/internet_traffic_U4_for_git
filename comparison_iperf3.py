import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def convert_to_byte(row):
    units = {'bytes': 1, 'kb': 1024, 'mb': 1024**2}

    try:
        ld_bytes_unit = str(row['ld_bytes_unit']).lower()
        factor = units[ld_bytes_unit]
        ld_kb = row['ld_bytes'] * factor

        rd_bytes_unit = str(row['rd_bytes_unit']).lower()
        factor = units[rd_bytes_unit]
        rd_kb = row['rd_bytes'] * factor

        total_bytes_unit = str(row['total_bytes_unit']).lower()
        factor = units[total_bytes_unit]
        total_kb = row['total_bytes'] * factor

        return pd.Series({'ld_bytes': ld_kb, 'rd_bytes': rd_kb, 'total_bytes': total_kb, 'server_ip': row['second_ip_interface']})
    except KeyError as e:
        print(f"Error processing row {row}: {e}")
        raise ValueError("Invalid unit. Supported units are 'bytes', 'kb', 'mb.")

df = pd.read_csv('iperf.txt', sep='\s+', skiprows=5, header=None, skipfooter=1, engine='python')

new_column_names = ["first_ip_interface", "arrow", "second_ip_interface", "ld_frames", "ld_bytes", "ld_bytes_unit",
                    "rd_frames", "rd_bytes", "rd_bytes_unit", "total_frames", "total_bytes", "total_bytes_unit",
                    "start", "duration"]

df.columns = new_column_names

df = df.assign(**df.apply(convert_to_byte, axis=1))

pd.set_option('display.max_columns', None)
print(df.head(2))

# Set y-axis limit based on the range of your data
y_min = df['total_bytes'].min()
y_max = df['total_bytes'].max()

# Plot all flows in the same figure with different colors based on the server_ip
plt.figure(figsize=(10, 6))

# Group by the unique combinations of 'first_ip_interface' and 'second_ip_interface'
groups = df.groupby(['first_ip_interface', 'second_ip_interface', 'server_ip'])

# Plot each group separately with different colors
for (name1, name2, server_ip), group in groups:
    if server_ip == '188.166.241.168:5201':
        plt.plot([group['start'], group['start'] + group['duration']], [group['total_bytes'], group['total_bytes']], color='blue', label='Target Server (active)')
    else:
        plt.plot([group['start'], group['start'] + group['duration']], [group['total_bytes'], group['total_bytes']], color='green',label='Other Servers (passive)')

plt.title('Active vs. passive of IPERF3')
plt.xlabel('Time')
plt.ylabel('Total Bytes')

# Set y-axis limit
plt.ylim(y_min-10, y_max)

# Set legend labels
plt.legend()
plt.show()
