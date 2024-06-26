import paramiko
# Adding/remove  jobs both work !!

def ssh_client_creation(host, port, username, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host, port=port, username=username, password=password)
    return ssh_client


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
    if test_cron(ssh_client, job) is True:
        if not job_exists(ssh_client, job):
            # Add the cron job
            stdin, stdout, stderr = ssh_client.exec_command(f'(crontab -l; echo "{job}") | crontab -', get_pty=True)
            print("Cron job added successfully!")
            print("Output:", stdout.read().decode().strip())
            print("Error:", stderr.read().decode().strip())
        else:
            print("Job already exists")
    else:
        print("Syntax Error:", test_cron(ssh_client, job))


def remove_cron(ssh_client, job):
    # Remove cron job
    fixed_cron = Fix(job)
    stdin, stdout, stderr = ssh_client.exec_command(f"crontab -l | grep -v '{fixed_cron}' | crontab -", get_pty=True)
    print("Cron job removed successfully!")
    print("Output:", stdout.read().decode().strip())
    print("Error:", stderr.read().decode().strip())

def print_active_jobs(ssh_client):
    stdin, stdout, stderr = ssh_client.exec_command("crontab -l")
    cron_output = stdout.read().decode().strip()
    return cron_output

# usage
    # if cron_output:
    #     print("Active cron jobs:")
    #     cron_list = cron_output.split('\n')
    #     for cron_job in cron_list:
    #         print(cron_job)
    # else:
    #     print("No active jobs")

def job_exists(ssh_client, job):
    stdin, stdout, stderr = ssh_client.exec_command("crontab -l")
    cron_output = stdout.read().decode().strip()
    if cron_output:
        cron_list = cron_output.split('\n')
        for cron_job in cron_list:
            if cron_job.strip() == job.strip():
                return True
    return False

def splitter(job):
    if job.split()[0].startswith('@'):
        schedule_expression, *command_parts = job.split(' ', 1)
        command = ' '.join(command_parts)
        return schedule_expression, command
    
    else:
        schedule_expression, command = job.split(' ', 5)[:5], job.split(' ', 5)[5:]
        return ' '.join(schedule_expression), ' '.join(command)
    

# exple usage
# if __name__ == "__main__":
#     host = '192.168.69.41'
#     port = 22 
#     username = 'manager1'
#     password = 'Pa$$w0rd'
#     jobs = ["@monthly /path/to/command2", "5 4 4-8 * * /path/to/test", "5 4 4,8 * * /path/to/command1", "* * * * * command1.sh", "* * * * * command1"]  
#     ssh_client = ssh_client_creation(host, port, username, password)  
    # for job in jobs:
        # add_cron(ssh_client, job)            

    # issue 1: if i delete job, it will delete both "* * * * * command1", and "* * * * * command1.sh" might leave it as is, coz i dont really care ngl  
    # Remove job
    # remove_cron(ssh_client, "@monthly /path/to/command2")
    # print_active_jobs(ssh_client)
    # Close SSH connection
    # ssh_client.close()