import socket 

print("scan force - the power of scanning")

ip = input("target:")

try:
    ip = socket.gethostbyname(ip)
except socket.gaierror:
    print("[-] Invalid IP or domain name")
    exit()



print("Starting TCP Connect Scan , 0-1024")
for port in range(0,1025):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.5)
    try:
        client.connect((ip,port))
        print(f"[+] {port} open")
    except :
        pass
    finally:
        client.close()    

