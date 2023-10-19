from scapy.all import rdpcap

def analyze_pcap(pcap_file):
    # Read the pcap file
    packets = rdpcap(pcap_file)

    # Calculate Size of trace file
    trace_file_size = sum(len(packet) for packet in packets)

    # Number of packets in trace file
    num_packets = len(packets)

    # Total size of packets
    total_packet_size = sum(len(packet) for packet in packets)

    return trace_file_size, num_packets, total_packet_size

if __name__ == "__main__":
    pcap_file_path = "U4_data4.pcap"
    trace_file_size, num_packets, total_packet_size = analyze_pcap(pcap_file_path)

    print(f"Size of trace file: {trace_file_size} bytes")
    print(f"Number of packets in trace file: {num_packets}")
    print(f"Total size of packets: {total_packet_size} bytes")


# Size of trace file: 266196265 bytes
# Number of packets in trace file: 227576
# Total size of packets: 266196265 bytes