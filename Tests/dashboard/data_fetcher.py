import json
import os
'''
Notes: 
-our monitoring is more about trend analysis or identifying long-term patterns (longer refresh times or averaging data might be more suitable)
'''

# this function will only append a new line to the json file
#now this function is pretty fast
def create_or_update_json(timestamp, LOAD1min, LOAD5min, LOAD15min, MachineName, CPUcores, CPUusage, RAMtotal, RAMusage, DISKtotal, DISKusage, UPTIME, NICnames, dataIN, dataOUT):
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

# expl usage for the function above
#create_or_update_json(f'2024-01-01 00:20:30', 1.2, 3.4, 5.6, 'MyMachine', 4, 30, 8192, 2048, 1024000, 512000, '10:00:00', ['NIC1', 'NIC2'], ['1000','200'], ['200','400'])
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
