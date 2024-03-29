import socket
import os

# Function to start execution
def start_execution():
    print("Execution started")
    with open('/home/server1/execution_started.txt', 'w') as file:
        file.write("Execution started\n")
    send_signal("EXECUTION_STARTED")

# Function to stop execution
def stop_execution():
    print("Execution stopped")
    with open('/home/server1/execution_stopped.txt', 'w') as file:
        file.write("Execution stopped\n")
    send_signal("EXECUTION_STOPPED")

# Function to delete a file
def delete_file(file_path):
    if os.path.isfile(file_path):
        os.remove(file_path)
        print(f"File '{file_path}' deleted")
        send_signal("FILE_DELETED")
    else:
        print(f"File '{file_path}' not found")
        send_signal("FILE_NOT_FOUND")

# Function to send a signal
def send_signal(signal):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('192.168.69.42', 6969))
        s.sendall(signal.encode())

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(('0.0.0.0', 6969))
        server_socket.listen(1)
        conn, _ = server_socket.accept()
        with conn:
            signal = conn.recv(1024).decode()
            if signal == "START":
                start_execution()
            elif signal == "STOP":
                stop_execution()
            elif signal.startswith("DELETE"):
                file_path = signal.split(' ')[1]
                delete_file(file_path)
            else:
                print(f"Unknown signal received: {signal}")
