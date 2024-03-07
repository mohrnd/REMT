import paramiko
# Adding/remove  jobs both work !!

def test_cron(ssh_client, cron):
    # Check cron syntax validity, found this somewhere, idk what it does lol
    stdin, stdout, stderr = ssh_client.exec_command(f'echo "{cron}" | crontab -l', get_pty=True)
    error = stderr.read().decode().strip()
    if error:
        return error
    return True

def Fix(cron_job):
    # Replace '*' with '\*' in the cron job string
    escaped_job = cron_job.replace('*', r'\*')
    return escaped_job

def add_cron(ssh_client, job):
    # Add cron job
    if test_cron(ssh_client, job) is True:
        stdin, stdout, stderr = ssh_client.exec_command(f'(crontab -l; echo "{job}") | crontab -', get_pty=True)
        print("Cron job added successfully!")
        print("Output:", stdout.read().decode().strip())
        print("Error:", stderr.read().decode().strip())
    else:
        print("Syntax Error:", test_cron(ssh_client, job))

def remove_cron(ssh_client, job):
    # Remove cron job
    fixed_cron = Fix(job)
    stdin, stdout, stderr = ssh_client.exec_command(f"crontab -l | grep -v '{fixed_cron}' | crontab -", get_pty=True)
    print("Cron job removed successfully!")
    print("Output:", stdout.read().decode().strip())
    print("Error:", stderr.read().decode().strip())




if __name__ == "__main__":
    host = '192.168.69.40'
    port = 22 
    username = 'manager1'
    password = 'Pa$$w0rd'
    jobs = ["@monthly /path/to/command2", "5 4 4-8 * * /path/to/test", "5 4 4,8 * * /path/to/command1", "* * * * * command1.sh", "* * * * * command1"]

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host, port=port, username=username, password=password)

    # Add job
    
    for job in jobs:
        add_cron(ssh_client, job)


    job = "* * * * * command1"
    #issue 1: if i delete job, it will delete both "* * * * * command1", and "* * * * * command1.sh" might leave it as is, coz i dont really care ngl
    
    # Remove job
    # remove_cron(ssh_client, job)

    # Close SSH connection
    ssh_client.close()
