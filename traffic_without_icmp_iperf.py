import csv

# 读取 CSV 文件
with open('result.csv', 'r') as csvfile:
    # 创建 CSV 读取器
    csvreader = csv.reader(csvfile)

    # 跳过标题行
    next(csvreader)

    # 初始化变量
    total_length = 0
    icmp_length = 0
    custom_info_length = 0

    # 遍历每一行
    for row in csvreader:
        # 获取长度字段
        length = int(row[5])

        # 计算整个文件中每个包的长度之和
        total_length += length

        # 计算使用 ICMP 协议的包的长度之和
        if row[4] == 'ICMP':
            icmp_length += length

        # 计算包含 '5201' 字符串的包的长度之和
        if '  5201 ' in row[6]:
            custom_info_length += length

# 打印结果
print(f"the length of all packets：{total_length} bytes")
print(f"the length of packets that use icmp：{icmp_length} bytes")
print(f"the length of packets that 5201 port：{custom_info_length} bytes")
print(f"traffic was there that was not iperf or ping traffic：{total_length-custom_info_length-icmp_length} bytes")
