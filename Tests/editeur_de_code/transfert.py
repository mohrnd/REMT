import paramiko

class Transfer:
    @staticmethod
    def PUT(hostname, username, password, localpath, remotepath):
        paramiko.util.log_to_file("REMT_PutsGets.log")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(hostname, username=username, password=password)
            sftp = ssh.open_sftp()
            sftp.put(localpath, remotepath)
            sftp.close()
            ssh.close()
            result_string = f"File '{localpath}' successfully sent to '{remotepath}'"
            return result_string
        except paramiko.AuthenticationException as auth_exception:
            return f"Authentication failed: {auth_exception}"
        except paramiko.SSHException as ssh_exception:
            return f"SSH connection failed: {ssh_exception}"
        except Exception as e:
            return f"An error occurred: {e}"

    @staticmethod
    def GET(hostname, username, password, localpath, remotepath):
        paramiko.util.log_to_file("REMT_PutsGets.log")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(hostname, username=username, password=password)
            sftp = ssh.open_sftp()
            sftp.get(remotepath, localpath)
            sftp.close()
            ssh.close()
            result_string = f"File '{remotepath}' successfully GETed to '{localpath}'"
            return result_string
        except paramiko.AuthenticationException as auth_exception:
            return f"Authentication failed: {auth_exception}"
        except paramiko.SSHException as ssh_exception:
            return f"SSH connection failed: {ssh_exception}"
        except Exception as e:
            return f"An error occurred: {e}"

#Example usage:
transfer = Transfer()
# result = transfer.PUT("192.168.69.38", "manager1", "Pa$$w0rd", r"C:\Users\BALLS2 (rip BALLS)\Desktop\REMT\Tests\manager GUI tests\REST GUI\rest logo\black.png", "/home/manager1/Desktop/black.png")
# print(result)
#result = transfer.GET("192.168.69.38", "manager1", "Pa$$w0rd", r"C:\Users\BALLS2 (rip BALLS)\Desktop\REMT\Tests\manager GUI tests\REST GUI\black.png", "/home/manager1/Desktop/black.png")
#print(result)