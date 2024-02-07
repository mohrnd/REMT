import getpass
from fabric import Connection, Config
from termcolor import colored

#fixed sudo and cd, everything should be working as intended, just need to do some more tests
##known issues:
#cat doesnt work sometimes, if the file doesnt exist it will close the ssh connection
#nano doesnt work
#when there is an error with a command, the ssh connection is closed
# ctrl + c sometimes doesnt work
# cat > filename, cant exit (ctrl + D doesnt work) and sometimes the text is duplicated 

hostname = "192.168.69.41"
port = 22
user = "server1"
password = "Pa$$w0rd"

config = Config(overrides={'sudo': {'password': password}})

def get_prompt(conn):
    result = conn.run('pwd', hide=True)
    cwd = result.stdout.strip()
    return colored(f'{user}@{hostname}:{cwd}$ ', 'green')

def exec_cmd(conn):
    while True:
        prompt = get_prompt(conn)
        command = input(prompt)
        if command.lower() == 'exit':
            break
        if "cd " in command:
            exec_cd(conn, command)
        elif "sudo " in command:
            exec_sudo(conn, command)
        else:
            result = conn.run(command)
            # print(result.stdout.strip())

def exec_cd(conn, cmd):
    directory = cmd.split("cd ")[1].strip()
    with conn.cd(directory):
        exec_cmd(conn)
        
def exec_sudo(conn, cmd):
    cmd_no_sudo = cmd.split("sudo ")[1].strip()
    result = conn.sudo(cmd_no_sudo)
    # print(result.stdout.strip())
    exec_cmd(conn)

try:
    with Connection(host=hostname, user=user, port=port, connect_kwargs={"password": password}, config=config) as conn:
        exec_cmd(conn)

except KeyboardInterrupt:
    print("\nExited by user.")
except Exception as e:
    print(f"An error occurred: {e}")

