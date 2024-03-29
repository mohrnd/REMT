import json

def merge_json(main_file, data_file):
    # Load JSON data from files
    with open(main_file, 'r') as f:
        main_data = json.load(f)
    with open(data_file, 'r') as f:
        data2 = json.load(f)
    
    # Create a dictionary for quick lookup of data2 values by time
    data2_dict = {entry['Time']: entry['Temperature'] for entry in data2}
    
    # Merge data
    merged_data = []
    main_index = 0
    data2_index = 0
    while main_index < len(main_data) or data2_index < len(data2):
        if main_index >= len(main_data):
            # If main data is exhausted, append remaining data2 entries
            while data2_index < len(data2):
                merged_data.append(data2[data2_index])
                data2_index += 1
        elif data2_index >= len(data2):
            # If data2 is exhausted, append remaining main data entries
            while main_index < len(main_data):
                merged_data.append(main_data[main_index])
                main_index += 1
        else:
            main_entry = main_data[main_index]
            data2_entry = data2[data2_index]
            if main_entry['Time'] == data2_entry['Time']:
                # If times match exactly, use main data entry
                merged_data.append(main_entry)
                main_index += 1
                data2_index += 1
            elif abs(main_entry['Time'] - data2_entry['Time']) <= 9:
                # If times are close, use data2 entry
                merged_data.append(data2_entry)
                main_index += 1
                data2_index += 1
            elif main_entry['Time'] < data2_entry['Time']:
                # If main entry time is before data2 entry time, use main entry
                merged_data.append(main_entry)
                main_index += 1
            else:
                # If data2 entry time is before main entry time, use data2 entry
                merged_data.append(data2_entry)
                data2_index += 1

    # Sort merged data by Time
    merged_data.sort(key=lambda x: x['Time'])
    
    # Write merged data back to main file
    with open(main_file, 'w') as f:
        json.dump(merged_data, f, indent=4)

# Paths to your JSON files
main_file = r'C:\Users\BALLS2 (rip BALLS)\Desktop\REMT\Tests\dashboard\merging_2_json_files\data_main.json'
data_file = r'C:\Users\BALLS2 (rip BALLS)\Desktop\REMT\Tests\dashboard\merging_2_json_files\data2.json'

merge_json(main_file, data_file)
