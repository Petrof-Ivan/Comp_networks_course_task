# from scapy.all import *
# import time
# from scapy import *

from scapy.all import *
from scapy.layers.inet import IP, UDP

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # hostname = "185.37.128.42"
    # hostname = "87.250.250.242"
    # 195.201.201.32
    hostname = input("Please, input IP address: ")
    print('|', hostname, '|')

    for i in range(1, 30):
        pkt = IP(dst=hostname, ttl=i) / UDP(dport=33434)
        reply = sr1(pkt, verbose=0, timeout=6)
        # print(type(reply))
        # отправляет пакет, ждет до первого ответа
        time.sleep(1)
        if reply is None:
            print("no reply", reply)
            break
        elif reply.type == 3:
            # Received ICMP dest-unreachable
            print("Done!", reply.src)
            break
        else:
            print(i, "  ", reply.src)
