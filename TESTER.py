from datetime import datetime, timedelta, timezone
aztz: timezone = timezone(timedelta(hours=-7), "AZ")
print(datetime.now().hour)
x = datetime.now() + timedelta(days=1)
print(datetime.now() < x)
