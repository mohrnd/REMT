import getpass
from fabric import Connection, Config

hostname = "192.168.69.41"
port = 22
user = "server1"
password = "Pa$$w0rd"

config = Config(overrides={'sudo': {'password': password}})

try:
    with Connection(host=hostname, user=user, port=port, connect_kwargs={"password": password}, config=config) as conn:
        while True:
            command = input('$>')
            if command.lower() == 'exit':
                break
            
            if "cd " in command:
                directory = command.split("cd ")[1].strip()
                with conn.cd(directory):
                    while True:
                        subcommand = input(f'{directory}$> ')
                        if subcommand.lower() == 'exit':
                            break
                        conn.run(subcommand)
            
            else:
                conn.run(command)
except KeyboardInterrupt:
    print("\nExited by user.")
except Exception as e:
    print(f"An error occurred: {e}")
