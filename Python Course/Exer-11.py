import time
from plyer import notification

current_time = time.localtime()
current_hour = current_time.tm_hour
current_min = current_time.tm_min
target_time = current_hour + 1

while True:
    current_time = time.localtime()
    if current_time.tm_hour == target_time:
        notification.notify(
            title='Drink Water!',
            message='Please Drink Water bro and take a short break!!',
            app_name='Drink Water!',
            timeout=30  # Increase the timeout to 30 seconds for better visibility
        )
        break
    else:
        time.sleep(60)
