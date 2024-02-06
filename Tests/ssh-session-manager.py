
#the following script can run commands on 2 different machines simultaneously

from ssh_session_manager.SSHSession import SSHSession
from ssh_session_manager.Command import Command
from ssh_session_manager.SSHSessionManager import SSHSessionManager

ssh_session_1 = SSHSession("Server1", "192.168.69.41", "server1", "Pa$$w0rd")
ssh_session_2 = SSHSession("Manager1", "192.168.69.45", "manager1", "Pa$$w0rd")
ssh_sessions = [ssh_session_1, ssh_session_2]


combined_command = "ls -la && cd Desktop && ls -la"

combined_ls_cd_update_command = Command(combined_command)

with SSHSessionManager(ssh_sessions) as ssh_session_manager:
    ssh_session_manager.run_commands_in_ssh_sessions([combined_ls_cd_update_command])
    command_output_dictionary = ssh_session_manager.get_command_output_dictionary(ssh_session_1, combined_ls_cd_update_command)
