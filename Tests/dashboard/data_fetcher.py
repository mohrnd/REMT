import json
import os
from fabric import Connection
import re
from datetime import datetime
import time
import threading
import csv
'''
Notes: 
-our monitoring is more about trend analysis or identifying long-term patterns (longer refresh times or averaging data might be more suitable)
'''


# this function will only append a new line to the json file
def create_or_update_json(data, MachineName):
    timestamp = data[0][0]
    LOAD1min = data[1][0]
    LOAD5min = data[2][0]
    LOAD15min = data[3][0]
    CPUcores = data[4][0]
    CPUusage = data[5][0]
    RAMtotal = data[6][0]
    RAMusage = data[7][0]
    DISKtotal = data[8][0]
    DISKusage = data[9][0]
    UPTIME = data[10][0]
    TotalSWAP = data[11][0]
    AvailableSWAP = data[12][0]
    TotalCachedMemory = data[13][0]
    NICnames = data[14]
    dataIN = data[15]
    dataOUT = data[16]
    data = {
        'timestamp': timestamp,
        'LOAD1min': LOAD1min,
        'LOAD5min': LOAD5min,
        'LOAD15min': LOAD15min,
        'CPUcores': CPUcores,
        'CPUusage': CPUusage,
        'RAMtotal': RAMtotal,
        'RAMusage': RAMusage,
        'DISKtotal': DISKtotal,
        'DISKusage': DISKusage,
        'UPTIME': UPTIME,
        'TotalSWAP':TotalSWAP, 
        'AvailableSWAP':AvailableSWAP,
        'TotalCachedMemory':TotalCachedMemory,
        'NICnames': NICnames,
        'dataIN': dataIN,
        'dataOUT': dataOUT
    }

    json_file_path = f'../REMT/tests/dashboard/{MachineName}.json'

    if not os.path.exists(json_file_path):
        with open(json_file_path, 'w') as file:
            json.dump([data], file, indent=4)
    else:
        with open(json_file_path, 'r+') as file:
            file.seek(0, 2)  # Move the file pointer to the end of the file
            file.seek(file.tell() - 1, 0)  # Move back one character to overwrite the closing square bracket
            file.write(',')  # Add a comma to separate the last item from the new item
            file.write(json.dumps(data, indent=4))  # Write the new JSON object
            file.write('\n]')  # Close the square brackets to maintain JSON format


def fetch_monitoring_data(SNMPv3_username, auth_Protocole, auth_password, Priv_Protocole, priv_password, security_engine_id, hostname, password, user, Port,  Machine_Name, RefreshTime):    
    while True:
        date_time = datetime.now()
        formated = date_time.strftime('%Y-%m-%d %H:%M:%S')
        conn = Connection(hostname, user=user, port=Port, connect_kwargs={"password": password})
        nothing = open(os.devnull, 'w')        
        OIDs = ['.1.3.6.1.4.1.2021.10.1.3.1', #1 minute Load 0
                '.1.3.6.1.4.1.2021.10.1.3.2', #5 minute Load 1
                '.1.3.6.1.4.1.2021.10.1.3.3', #15 minute Load 2
                '1.3.6.1.2.1.25.3.3.1.2', #Number of CPU cores 3
                '.1.3.6.1.4.1.2021.11.52.0', #raw system cpu time 4
                '.1.3.6.1.4.1.2021.4.5.0', #Total RAM in machine 5
                '.1.3.6.1.4.1.2021.4.6.0', #Total RAM used 6
                '.1.3.6.1.4.1.2021.9.1.6.1', #Total size of the disk (kBytes) 7
                '1.3.6.1.4.1.2021.9.1.9.1', #Disk usage Pourcentage 8
                '.1.3.6.1.2.1.1.3.0', #System Uptime 9
                '.1.3.6.1.4.1.2021.4.3.0', #Total Swap Size 10
                '.1.3.6.1.4.1.2021.4.4.0', #Available Swap Space 11
                '.1.3.6.1.4.1.2021.4.15.0', #Total Cached Memory 12
                '.1.3.6.1.2.1.2.2.1.2' , #NIC names 13
                '.1.3.6.1.2.1.2.2.1.10', #Bytes IN 14
                '.1.3.6.1.2.1.2.2.1.16', #Bytes OUT 15
                ]
        outputs = []
        for OID in OIDs:
            output = conn.run(f'snmpwalk -v3 -l authPriv -u {SNMPv3_username} -a {auth_Protocole} -A {auth_password} -x {Priv_Protocole} -X {priv_password} {hostname} {OID}', warn=True, out_stream=nothing)
            values = re.findall(r'(?<=STRING: )\S+|(?<=Counter32: )\d+|(?<=INTEGER: )\d+|(?<=Timeticks: \()\d+', output.stdout)
            outputs.append(values)
        outputs[3] = [f'{len(outputs[3])}']
        total_ram_used = int(outputs[6][0])  
        total_ram_in_machine = int(outputs[5][0]) 
        ram_percentage = (total_ram_used / total_ram_in_machine) * 100  
        outputs[6] = [f'{ram_percentage:.0f}'] 
        outputs.insert(0,[formated])
        current_cpu_time = int(outputs[5][0])
        system_uptime = int(outputs[10][0])
        system_uptime_seconds = system_uptime // 100
        number_of_cores = int(outputs[4][0])
        cpu_usage_per_second_per_core = current_cpu_time / system_uptime_seconds / number_of_cores
        cpu_usage_percentage = cpu_usage_per_second_per_core * 100
        outputs[5] =  [f'{cpu_usage_percentage:.0f}'] 
        nothing.close()
        create_or_update_json(outputs, Machine_Name)
        
        time.sleep(int(RefreshTime)-2)
    
#test:
# # fetch_monitoring_data('roadmin', 'SHA', 'admin123', 'AES', 'admin123', 'nothin', '192.168.69.47', 'Pa$$w0rd', 'server1', 22,  'server1', 5)
# params1 = ('roadmin', 'SHA', 'admin123', 'AES', 'admin123', 'nothin', '192.168.69.47', 'Pa$$w0rd', 'server1', 22,  'server1', 15)
# params2 = ('roadmin', 'SHA', 'admin123', 'AES', 'admin123', 'nothin', '192.168.69.47', 'Pa$$w0rd', 'server1', 22,  'server2', 15)

# # Create threads for each instance
# thread1 = threading.Thread(target=fetch_monitoring_data, args=params1)
# thread2 = threading.Thread(target=fetch_monitoring_data, args=params2)

# # Start the threads
# thread1.start()
# thread2.start()

# # Wait for both threads to finish
# thread1.join()
# thread2.join()

def read_params_from_csv(csv_file):
    params = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            params.append(row)
    return params

def monitor_params_threads_creator(csv_file):
    existing_params = set()
    while True:
        new_params = read_params_from_csv(csv_file)
        for params in new_params:
            params_key = tuple(params)
            if params_key not in existing_params:
                thread = threading.Thread(target=fetch_monitoring_data, args=params)
                thread.start()
                existing_params.add(params_key)
        time.sleep(60) # checks the users file for any new changes

def main():
    csv_file = r'C:\Users\BALLS2 (rip BALLS)\Desktop\REMT\Tests\network monitoring\snmp tests\snmp_users.csv'
    monitor_thread = threading.Thread(target=monitor_params_threads_creator, args=(csv_file,))
    monitor_thread.start()






# expl usage for the function above
#create_or_update_json(timestamp, LOAD1min, LOAD5min, LOAD15min, MachineName, CPUcores, CPUusage, RAMtotal, RAMusage, DISKtotal, DISKusage, UPTIME,TotalSWAP, AvailableSWAP, TotalCachedMemory, NICnames, dataIN, dataOUT)
# idk might find a use for this later
def timestamp_finder(json_file_path, target):
    with open(json_file_path, 'r') as file:
        existing_data = json.load(file)        
        for entry in existing_data:
            if entry['timestamp'] == target:
                return entry
        else:
            return f"No data found for timestamp {target}"


# this function will be used only when drawing graphs (to sort the whole file, it is pretty fast so i dont mind executing it everytime a graph is drawn)
def sort_json_file_by_timestamp(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    sorted_data = sorted(data, key=lambda x: x['timestamp'])
    with open(json_file_path, 'w') as file:
        json.dump(sorted_data, file, indent=4)


if __name__ == "__main__":
    main()