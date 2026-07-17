import subprocess
import re
import socket

ports = [21, 22, 80, 443, 8080]
active_ips = []

result = subprocess.run(["arp", "-an"], capture_output=True, text=True)

found_ips = re.findall(r"\((192\.168\.100\.\d+)\)", result.stdout)

for ip in found_ips:
    if not ip.endswith(".255"):
        print(f"New device with ip - {ip}")
        active_ips.append(ip)

for ip in active_ips:
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)
        try:
            s.connect((ip, port))
            print(f"Port {port} is open for {ip}")
        except socket.error:
            pass
        finally:
            s.close()