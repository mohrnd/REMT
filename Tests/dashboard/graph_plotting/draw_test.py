import json
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Path to your JSON file
json_file = r"C:\Users\BALLS2 (rip BALLS)\Desktop\REMT\Tests\dashboard\Machine1.json"

# Function to parse timestamp to datetime object
def parse_timestamp(timestamp):
    return datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")

# Load JSON data
with open(json_file, 'r') as f:
    data = json.load(f)

# Extract LOAD1min and timestamp data
load1min_data = []
timestamps = []
for entry in data:
    load1min_data.append(entry["LOAD1min"])
    timestamps.append(parse_timestamp(entry["timestamp"]))

# Calculate average LOAD1min for each 1-hour interval
interval_start = timestamps[0]
interval_end = interval_start + timedelta(hours=1)
averages = []
average_timestamps = []

total_load1min = 0
count = 0
i = 0
while i < len(timestamps):
    if interval_start <= timestamps[i] < interval_end:
        total_load1min += load1min_data[i]
        count += 1
    elif timestamps[i] >= interval_end:
        if count > 0:
            averages.append(total_load1min / count)
            average_timestamps.append(interval_start)
        
        # Move to the next interval
        interval_start = interval_end
        interval_end += timedelta(hours=1)
        
        total_load1min = 0
        count = 0
        continue
    
    i += 1

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(average_timestamps, averages, marker='o', linestyle='-')
plt.title('Average LOAD1min per Hour')
plt.xlabel('Time')
plt.ylabel('Average LOAD1min')
plt.xticks(rotation=90)
plt.grid(True)
plt.tight_layout()

# Display the plot
plt.show()
