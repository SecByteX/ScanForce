import socket 

print("Welcome to port scanner application...")
ip = input("target:")



print("Starting TCP Connect Scan")
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
        
    

    

