from cron_descriptor import get_description
from croniter import croniter
from datetime import datetime, timedelta

def next_run_for_annotation(annotation):
    now = datetime.now()
    if annotation == "@yearly" or annotation == "@annually":
        next_run = now.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0) + timedelta(days=366 if now.year % 4 == 0 else 365)
    elif annotation == "@monthly":
        next_run = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0) + timedelta(days=32)
        next_run = next_run.replace(day=1)
    elif annotation == "@weekly":
        days_until_next_target_weekday = ((7 - now.weekday()) % 7)+6
        next_run = now + timedelta(days=days_until_next_target_weekday)
        next_run = datetime(next_run.year, next_run.month, next_run.day, 0, 0)
    elif annotation == "@daily" or annotation == "@midnight":
        next_run = now + timedelta(days=1, hours=-now.hour, minutes=-now.minute, seconds=-now.second, microseconds=-now.microsecond)
    elif annotation == "@hourly":
        next_run = now + timedelta(hours=1, minutes=-now.minute, seconds=-now.second, microseconds=-now.microsecond)
    elif annotation == "@reboot":
        next_run = "Au redémarrage avec les droits utilisateurs"
    else:
        next_run = None
    return next_run

def interpret_schedule(schedule_input):
    try:
        expression_description = get_description(schedule_input)

        now = datetime.now()
        cron = croniter(schedule_input, now)
        next_run = cron.get_next(datetime)

        print("Interpretation of the cron expression: ")
        print(expression_description)
        print("Next planned execution: ", next_run)
    except Exception as e:
        
        schedule_annotations = {
            "@yearly": "Every year",
            "@annually": "Every year",
            "@monthly": "Every month at midnight",
            "@weekly": "Every week",
            "@daily": "Every day at midnight",
            "@midnight": "Every night at midnight",
            "@hourly": "Every hour",
            "@reboot": "When restarting with user rights"
        }

        if schedule_input in schedule_annotations:
            print("Interpretation of the planning annotation: ")
            print(schedule_annotations[schedule_input])
            next_run = next_run_for_annotation(schedule_input)
            print("Next planned execution: ", next_run)
        else:
            print("Unable to interpret input.")

if __name__ == "__main__":
    user_input = input("Please enter a cron expression or scheduling annotation: ")
    interpret_schedule(user_input)