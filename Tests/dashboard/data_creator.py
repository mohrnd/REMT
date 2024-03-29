import json
import os

def create_or_update_json_batch(data_list, machine_name):
    json_file_path = f'../REMT/tests/dashboard/{machine_name}.json'
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as file:
            existing_data = json.load(file)
    else:
        existing_data = []

    existing_data.extend(data_list)

    with open(json_file_path, 'w') as file:
        json.dump(existing_data, file, indent=4)

def generate_data(machine_name, start_month, end_month):
    data_list = []
    linenumber = 0
    for month in range(start_month, end_month + 1):
        for day in range(1, 32):
            for hour in range(0, 24):
                for minute in range(0, 60):
                    for second in range(0, 60, 30):
                        linenumber += 25
                        timestamp = f'2024-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}'
                        data = {
                            'timestamp': timestamp,
                            'LOAD1min': 1.2,
                            'LOAD5min': 3.4,
                            'LOAD15min': 5.6,
                            'CPUcores': 4,
                            'CPUusage': 30,
                            'RAMtotal': 8192,
                            'RAMusage': 2048,
                            'DISKtotal': 1024000,
                            'DISKusage': 512000,
                            'UPTIME': '10:00:00',
                            'NICnames': ['NIC1', 'NIC2'],
                            'dataIN': ['1000', '200'],
                            'dataOUT': ['200', '400']
                        }
                        data_list.append(data)
                        print(f'{timestamp} line number {linenumber} added!')
    return data_list

# Generate data for two months (January and February)
machine_name = 'MyMachine'
start_month = 1
end_month = 2
data_list = generate_data(machine_name, start_month, end_month)

# Insert data into JSON file in batch
create_or_update_json_batch(data_list, machine_name)
