import paramiko
import time

# kinda bad, will use fabric from now on
#the issue with this is when i run a sudo dnf update, the installation is not being updated in real time

wait_time = 1

def ssh_interactive_shell():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('192.168.69.41', username='root', password='Pa$$w0rd', port=22)
    channel = ssh.invoke_shell()
    output = channel.recv(9999)
    print(output.decode("utf-8"), end='')
    print("Press enter")
    while True:
        command = input('')
        if command.lower() == 'exit':
            break
        ######################################################
        channel.send(command + '\n')
        # Wait for a brief moment to allow command to be executed
        time.sleep(wait_time)
        # Receive output
        output = channel.recv(9999)
        print(output.decode("utf-8"), end='')
        ######################################################
    ssh.close()

if __name__ == "__main__":
    ssh_interactive_shell()
