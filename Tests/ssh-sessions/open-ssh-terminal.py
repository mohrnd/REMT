import subprocess

#works (requires a password once)
##steps:
#on the manager exec: ssh-keygen -t rsa
#send the key to the server we want to ssh into using: ssh-copy-id server1@ip
#now i can directly ssh without needing a password everytime


def open_ssh_terminal(user, ip):
    ssh_command = f"ssh {user}@{ip}"  
    subprocess.run(['gnome-terminal', '--', 'bash', '-c', ssh_command])  

open_ssh_terminal("server1","192.168.69.41")