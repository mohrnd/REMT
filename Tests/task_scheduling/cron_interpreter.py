import croniter
import datetime

def cron_to_description(cron_expression):
    try:
        cron = croniter.croniter(cron_expression)
        description = f"Every {cron.get_next(datetime.datetime).strftime('%A')} at {cron.get_next(datetime.datetime).strftime('%I:%M %p')}"
        return description
    except:
        return "Invalid cron expression"

# Example usage
cron_expression = "1 */2 * * 2"
description = cron_to_description(cron_expression)
print(description) 

# MIN, HOURS AND DAY OF THE WEEK ALL WORK NICELY
# / , AND - DONT WORK
# DAY OF MONTH AND MONTH DONT WORK