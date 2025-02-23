import socket

target = input("Enter target IP: ")
ports = [21, 22, 23, 25, 53, 80, 443, 3306]

print(f"Scanning {target}...")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")
    sock.close()
