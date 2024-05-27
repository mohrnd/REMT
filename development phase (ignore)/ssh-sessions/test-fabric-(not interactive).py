from fabric import Connection

hostname = '192.168.69.40'
user = 'root'
port = 22 
password = 'Pa$$w0rd' 
cron_job = '*/5 * * * 2 perl /home/mobman/wad2.pl'


conn = Connection(hostname, user=user, port=port, connect_kwargs={"password": password})

result = conn.run(f'echo "{cron_job}" >> /var/spool/cron/{user}', warn=True)

if result.exited != 0:
    print("Failed to add cron job:", result.stderr)
else:
    print("Cron job added successfully.")
