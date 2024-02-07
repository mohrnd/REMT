import paramiko
import sys
import select
import tty
import termios #only on linux, coz windows is not a POSIX platform
import socket

#we need to create a pseudo-terminal (PTY) on the SSH server
#wont work on windows, only linux
#closest thing we have to an interactive ssh


def ssh_connect(hostname, username, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_client.connect(hostname, username=username, password=password)
        print("SSH connection established to", hostname)
        return ssh_client
    except paramiko.AuthenticationException:
        print("Authentication failed for", username, "@", hostname)
        sys.exit(1)
    except paramiko.SSHException as e:
        print("SSH connection failed to", hostname, ":", e)
        sys.exit(1)

def shell(channel):
    oldtty = termios.tcgetattr(sys.stdin)
    try:
        tty.setraw(sys.stdin.fileno())
        tty.setcbreak(sys.stdin.fileno())
        channel.settimeout(0.0)

        while True:
            r, w, e = select.select([channel, sys.stdin], [], [])
            if channel in r:
                try:
                    x = channel.recv(1024)
                    if len(x) == 0:
                        print("\r\n*** EOF\r\n")
                        break
                    sys.stdout.write(x.decode())
                    sys.stdout.flush()
                except socket.timeout:
                    pass
            if sys.stdin in r:
                x = sys.stdin.read(1)
                if len(x) == 0:
                    break
                channel.send(x)
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)

if __name__ == "__main__":
    # Provide SSH credentials and server information
    hostname = "192.168.69.41"
    username = "server1"
    password = "Pa$$w0rd"

    ssh_client = ssh_connect(hostname, username, password)
    transport = ssh_client.get_transport()
    channel = transport.open_session()
    channel.get_pty()
    channel.invoke_shell()
    shell(channel)
    channel.close()
    ssh_client.close()
