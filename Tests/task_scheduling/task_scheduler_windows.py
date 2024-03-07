import paramiko
# Adding jobs works !!
# Removing jobs doesnt work

def test_cron(ssh_client, cron):
    # Check cron syntax validity
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
    # SSH credentials and job
    host = '192.168.69.40'
    port = 22  # Default SSH port
    username = 'manager1'
    password = 'Pa$$w0rd'
    jobs = ["*/5 * * * * /path/to/command2", "*/5 * * * * /path/to/test", "*/5 * * * * /path/to/command1"]

    # Connect to remote machine
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host, port=port, username=username, password=password)

    # Add job
    # for job in jobs:
    #     add_cron(ssh_client, job)


    job = "*/5 * * * * /path/to/command1"
    # Remove job
    remove_cron(ssh_client, job)

    # Close SSH connection
    ssh_client.close()
