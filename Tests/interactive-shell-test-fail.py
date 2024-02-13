import paramiko
import getpass

def interactive_shell(channel):
    try:
        while True:

            command = input("")

            if command.strip() == 'exit':
                break
            channel.send(command + '\n')

            while channel.recv_ready():
                print(channel.recv(1024).decode('utf-8'), end='')
    except KeyboardInterrupt:
        print("\nExiting...")


hostname = "192.168.69.41"
username = "server1"
password = getpass.getpass("Enter password: ")


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    client.connect(hostname, username=username, password=password)

    channel = client.invoke_shell()

    interactive_shell(channel)

finally:

    client.close()
