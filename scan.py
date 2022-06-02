import socket 
import threading

def port_scanner(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        print(f"Port {port} is open")
    except:
        pass
print("type ip address below (ip only no hostname)")
address = input()

target = (address)   # scan local host

for port in range(1,5050):
    thread = threading.Thread(target =port_scanner, args=[port])
    thread.start()
