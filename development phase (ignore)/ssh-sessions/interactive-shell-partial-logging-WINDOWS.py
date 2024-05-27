import paramiko
import sys
import getpass
import threading
import socket
import logging
import os
import re
import msvcrt #used for handling console input/output and keyboard events in Windows environments.
#is an alternative to termios

logging.basicConfig(filename='ssh2.log', level=logging.INFO, format='%(asctime)s - %(message)s')

PASSWORD_PROMPT_PATTERN = re.compile(r'[Pp]assword:?\s*$')

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
        print("Establishing SSH Connection...")
        ssh_client.connect(hostname, username=username, password=password)
        current_user = os.getenv("USERNAME")
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

def shell(channel):
    while True:
        try:
            if msvcrt.kbhit(): #returns a non-zero value if a keypress is waiting to be read
                ch = msvcrt.getch() #reads a single character from the console without echoing it to the screen and without buffering
                if ch == b'\x03':  # Ctrl+C
                    channel.send('\x03')
                elif ch == b'\x04':  # Ctrl+D
                    channel.send('\x04')
                else:
                    channel.send(ch)
        except IOError:
            pass

def read_ssh_output(channel):
    while True:
        try:
            x = channel.recv(1024)
            if not x:
                break
            sys.stdout.write(x.decode('utf-8', errors='ignore'))
            sys.stdout.flush()
        except socket.timeout:
            pass

if __name__ == "__main__":
    hostname = "192.168.69.44"
    username = "server1"
    password = "Pa$$w0rd"

    ssh_client = ssh_connect(hostname, username, password)
    transport = ssh_client.get_transport()
    channel = transport.open_session()
    channel.get_pty()
    channel.invoke_shell()

    output_thread = threading.Thread(target=read_ssh_output, args=(channel,))
    output_thread.daemon = True
    output_thread.start()

    shell(channel)

    channel.close()
    ssh_client.close()
