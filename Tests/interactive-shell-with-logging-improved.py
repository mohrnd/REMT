import paramiko
import sys
import select
import tty
import termios #only on linux, coz windows is not a POSIX platform
import socket
from time import sleep
from tqdm import tqdm
import logging
import os
import re
#we need to create a pseudo-terminal (PTY) on the SSH server
#wont work on windows, only linux
#closest thing we have to an interactive ssh
logging.basicConfig(filename='ssh2.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def ssh_connect(hostname, username, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        print("    ____  _________________")
        print("   / __ \/ ____/ ___/_  __/")
        print("  / /_/ / __/  \__ \ / /   ")
        print(" / _  _/ /___ ___/ // /    ")
        print("/_/ |_/_____//____//_/     ")
        print("")
        print("Remote Execution and Security Toolkit")
        print("")
        var = 50
        for _ in tqdm(range(var), desc="Establishing SSH Connection", bar_format="{l_bar}{bar}{r_bar}", ascii=True, colour='red'):
            sleep(0.01)
        ssh_client.connect(hostname, username=username, password=password)
        current_user = os.getenv("USER") or os.getlogin()
        logging.info(f"SSH connection established to {hostname} by user {current_user}")
        print("SSH connection established to", hostname)
        
        return ssh_client
    except paramiko.AuthenticationException:
        print("Authentication failed for", username, "@", hostname)
        logging.error(f"Authentication failed for {username}@{hostname} established by {current_user}")
        sys.exit(1)
    except paramiko.SSHException as e:
        print("SSH connection failed to", hostname, ":", e)
        logging.error(f"SSH connection established by {current_user} failed {hostname}: {e}")
        sys.exit(1)
PASSWORD_PROMPT_PATTERN = re.compile(r'[Pp]assword:?\s*$')

def shell(channel):
    oldtty = termios.tcgetattr(sys.stdin)
    try:
        tty.setraw(sys.stdin.fileno()) #Character-by-character input, Disabling line buffering, Disabling echo, Control characters. This is essential for creating an interactive shell-like environment 
        tty.setcbreak(sys.stdin.fileno())
        channel.settimeout(0.0)  #makes the channel non-blocking, meaning that operations on the channel will not wait for data to be available before returning
        command_buffer = ""
        password_input = False  # Flag to track if password input is in progress
        while True:
            r, w, e = select.select([channel, sys.stdin], [], []) #allows the script to monitor multiple file descriptors for read, write, and error events simultaneously.
            
            if channel in r:
                try:
                    x = channel.recv(1024)
                    if len(x) == 0:
                        print("\r\n*** EOF\r\n")
                        break
                    sys.stdout.write(x.decode()) #this line gets the input/output of the ssh (tab autocomplete too)
                    
                    if not password_input:
                        logging.info(f"[Server]: {x.decode().strip()}")

                    sys.stdout.flush()

                    # Check if the server response contains a password prompt
                    if not password_input and PASSWORD_PROMPT_PATTERN.search(x.decode()):
                        logging.info("Password input requested by the server. Logging paused.")
                        password_input = True
                except socket.timeout:
                    pass
            if sys.stdin in r and not password_input:
                x = sys.stdin.read(1) #reads user input only
                if len(x) == 0:
                    break
                elif x == '\r':
                    if 'sudo' not in command_buffer:
                        logging.info(f"Command executed by [{os.getenv('USER')}]: {command_buffer}")
                        command_buffer = ""
                else:
                    command_buffer += x
                
                channel.send(x)

            if sys.stdin in r and password_input:
                x = sys.stdin.read(1) #reads user input only
                if x == '\r':
                    password_input = False
                continue
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)

if __name__ == "__main__":
    hostname = "192.168.69.44"
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

#security vulnerabilities:
#Password-based Authentication
#No Transport Layer Security (TLS): The script uses SSH for secure communication, but it does not use TLS for securing the initial connection.
#ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) must be removed


