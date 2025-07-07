import socket 
import argparse

print("scan force - the power of scanning")

parser = argparse.ArgumentParser(description="TCP Connect Port Scanner")
parser.add_argument("--target",required=True,help="Target IP/Domain")
parser.add_argument("--ports",default="1-1024",help="Port range (e.g 20-40)")
args = parser.parse_args()

try:
    ip = socket.gethostbyname(args.target)
except socket.gaierror:
    print("[-] Invalid IP or domain name")
    exit()


try :
    start_port , end_port = map(int, args.ports.split("-"))
except:
    print("[-] Invalid Port Range (e.g. 20-40)")
    exit()

for port in range(start_port,end_port+1):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.5)
    try:
        client.connect((ip,port))
        print(f"[+] {port} open")
    except :
        pass
    finally:
        client.close()    

