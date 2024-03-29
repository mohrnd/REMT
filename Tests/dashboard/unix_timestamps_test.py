
from datetime import datetime
import time


date_time = datetime.now()
formated = date_time.strftime('%Y-%m-%d %H:%M:%S')

print("date_time =>",formated)
print("unix_timestamp => ",(int(time.mktime(date_time.timetuple()))))
