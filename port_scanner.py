import socket
import threading

target = "pythonprogramming.net"
ip = socket.gethostbyname(target)
print(ip)


def portscan(port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.settimeout(1)

    try:
        r = s.connect_ex((target, port))

        if r == 0:
            print("Port :", port, "is open.")

        s.close()
    except socket.gaierror:
        pass

    except ConnectionRefusedError:
        pass

    except socket.timeout:
        pass


r = 1
for x in range(1, 443):

    t = threading.Thread(target=portscan, kwargs={"port": r})
    # t.daemon = True

    r += 1
    t.start()
