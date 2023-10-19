import subprocess
import time


def ping_and_save(addr, output_file):
    formatted_datetime = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(output_file, 'a') as f:
        f.write(formatted_datetime + '\n')

    # Run ping command with a timeout of 5 seconds
    try:
        result = subprocess.run(['ping', '-n', '5', addr], capture_output=True, timeout=5, text=True)
        with open(output_file, 'a') as f:
            f.write(result.stdout + '\n')
    except subprocess.TimeoutExpired:
        with open(output_file, 'a') as f:
            f.write("Ping timed out\n")


addr1 = "ok1.iperf.comnet-student.eu" #195.148.124.36
addr2 = "sgp1.iperf.comnet-student.eu" #188.166.241.168
addr3 = "anycastdns2.nic.td" #185.28.194.194
addr4 = "ns-td.afrinic.net" #196.216.168.31
addr5 = "pch.nic.td" #204.61.216.129

ping_and_save(addr1, "ping\\" + addr1 + ".txt")
ping_and_save(addr2, "ping\\" + addr2 + ".txt")
ping_and_save(addr3, "ping\\" + addr3 + ".txt")
ping_and_save(addr4, "ping\\" + addr4 + ".txt")
ping_and_save(addr5, "ping\\" + addr5 + ".txt")
