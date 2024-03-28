import csv, os



'''
for now the dashboard will contain:

-MACHINE STATUS (ONLINE/OFFLINE)
-number of CPU cores
-ammount of RAM in total, and in use
-ammount of DISK space in total, ammount in current use, generate a notif if the disk space is getting low
-UPTIME (daily average uptime, weekly average uptime, monthly average uptime)
-BANDWIDTH USAGE MONITOR
-ping ?

'''


def create_or_update_csv(time, LOAD1min,LOAD5min,LOAD15min, MachineName, CPUcores, CPUusage, RAMtotal, RAMusage, DISKtotal, DISKusage, UPTIME, TRAP, BWusage):
    columns = ['time',
               'LOAD1min',
               'LOAD5min',
               'LOAD15min',
               'CPUcores', 
               'CPUusage', 
               'RAMtotal',
               'RAMusage',
               'DISKtotal',
               'DISKusage',
               'UPTIME', 
               'TRAP',
               'BWusage']
    data = [time,LOAD1min,LOAD5min,LOAD15min, CPUcores, CPUusage, RAMtotal, RAMusage, DISKtotal, DISKusage , UPTIME, TRAP, BWusage]

    csv_file_path = f'../REMT/tests/dashboard/{MachineName}.csv'
    if not os.path.exists(csv_file_path):
        with open(csv_file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(columns)
            
    with open(csv_file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

