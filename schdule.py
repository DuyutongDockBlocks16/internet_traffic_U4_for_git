import schedule
import time
import subprocess

def run_ping_script():
    subprocess.run(['python', 'ping.py'])

def run_iperf3_script():
    subprocess.run(['.\iperf3.bat'])

# 创建每分钟执行一次 run_ping_script 的任务
ping_job = schedule.every(1).minutes.do(run_ping_script)

# 创建每分钟执行一次 run_iperf3_script 的任务
iperf3_job = schedule.every(1).minutes.do(run_iperf3_script)

while True:
    schedule.run_pending()
    time.sleep(1)


# dumpcap -i "WLAN" -w "D:\0x02_LearningAndWorking\Aalto\U4_data3.pcap"
# Get-NetAdapterStatistics -Name "WLAN"