Create a wrapper script (e.g., wrapper_shutdown_terminal.sh):

#!/bin/bash
python3 /path/to/shutdown_terminal.py


Make the script executable:
chmod +x wrapper_shutdown_terminal.sh

Move the wrapper script to the appropriate directory:
sudo mv wrapper_shutdown_terminal.sh /usr/local/bin/

Replace the original shutdown and reboot executables with symbolic links to the wrapper script:
sudo ln -sf /usr/local/bin/wrapper_shutdown_terminal.sh /sbin/shutdown
sudo ln -sf /usr/local/bin/wrapper_shutdown_terminal.sh /sbin/reboot
This effectively replaces the native shutdown and reboot commands with your wrapper script.

to undo the links: 
sudo rm /sbin/reboot  
sudo ln -s /bin/systemctl /sbin/reboot  


The above didnt work, i will try something else at a later date.

read last line of the log file:
tac Shutdown.log | head -n 1