from datetime import datetime
import os
import subprocess
reason = input("Please enter the reason why you need to turn off the server: ")

confirmation = input("Are you sure you want to continue? (y/n): ")

if confirmation.lower() == 'y':
    log_file = "/var/log/Shutdown.log"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    username = os.getlogin()

    log_entry = f"{timestamp} | User: {username} | Reason: {reason}\n"

    with open(log_file, "a") as file:
        file.write(log_entry)
        subprocess.run(['/usr/local/bin/shutdown.sh'], check=True)
else:
    print("Shutdown canceled.")

# Notes:
#The logging worked, the shutdown didnt