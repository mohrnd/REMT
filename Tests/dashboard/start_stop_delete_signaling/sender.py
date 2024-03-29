import socket

SERVER_IP = '192.168.69.47' 
SERVER_PORT = 6969  

def handle_signal(signal):
    print("Received signal:", signal)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect((SERVER_IP, SERVER_PORT))
    
    signal = "STOP"
    print("Sending signal:", signal)
    s.sendall(signal.encode())

    while True:
        signal = s.recv(1024).decode()
        if not signal:
            break
        handle_signal(signal)
