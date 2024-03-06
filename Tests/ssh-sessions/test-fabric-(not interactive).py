import getpass
from fabric import Connection, Config
from termcolor import colored

# fixed sudo and cd, everything should be working as intended, just need to do some more tests
#issue in the script below: command outputs are being printed 2 times


hostname = "192.168.69.40"
port = 22
user = "manager1"
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
            result = conn.run(command, warn=True)
            if result.exited:
                print(colored(f"Command exited with status {result.exited}", 'red'))
            if result.stdout:
                print(result.stdout.strip())
            if result.stderr:
                print(colored(result.stderr.strip(), 'red'))

def exec_cd(conn, cmd):
    directory = cmd.split("cd ")[1].strip()
    with conn.cd(directory):
        pass

def exec_sudo(conn, cmd):
    cmd_no_sudo = cmd.split("sudo ")[1].strip()
    result = conn.sudo(cmd_no_sudo, warn=True)
    if result.exited:
        print(colored(f"Command exited with status {result.exited}", 'red'))
    if result.stdout:
        print(result.stdout.strip())
    if result.stderr:
        print(colored(result.stderr.strip(), 'red'))

try:
    with Connection(host=hostname, user=user, port=port, connect_kwargs={"password": password}, config=config) as conn:
        conn.sudo('dnf install gedit', warn=True)# exec_cmd(conn)

except KeyboardInterrupt:
    print("\nExited by user.")
except Exception as e:
    print(f"An error occurred: {e}")
