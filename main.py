
import socket


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # hostname = "185.37.128.42"
    # hostname = "87.250.250.242"
    # 195.201.201.32

    IP = input("Please, input IP address:")
    PORT = 33436
    TTL = 1
    HOPS = 30
    # MESSAGE = "Hello, World!"

    print("target IP:", IP)
    print("target port:", PORT)
    # print("message:", MESSAGE)

    # sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
    # sock.sendto(bytes(MESSAGE, "utf-8"), (IP, PORT))

    while True:
        r = socket.socket(
            family=socket.AF_INET,
            type=socket.SOCK_RAW,
            proto=socket.IPPROTO_ICMP
        )
        try:
            r.bind(('', PORT))
        except socket.error as e:
            raise IOError('Unable to bind receiver socket: {}'.format(e))

        s = socket.socket(
            family=socket.AF_INET,
            type=socket.SOCK_DGRAM,
            proto=socket.IPPROTO_UDP
        )
        s.setsockopt(socket.SOL_IP, socket.IP_TTL, TTL)

        s.sendto(b'', (IP, PORT))
        src_ip = None
        try:
            data, src_ip = r.recvfrom(1024)
            # print(data[0].decode())
        except socket.error:
            raise IOError('Socket error: {}'.format(e))
        finally:
            r.close()
            s.close()

        if src_ip:
            print(TTL, '    ', src_ip[0])
        else:
            print(TTL, '    ***')

        TTL = TTL + 1

        if src_ip[0] == IP:
            print('Done!', src_ip[0])
            break
        if TTL > 30:
            break
