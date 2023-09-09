import psutil
from datetime import datetime
from time import sleep
import socket

while True:
    interval = input("Enter monitoring period(sec): ")
    if interval.isdigit():
        interval = int(interval)
        break
    else:
        print("Enter a number")
while True:
    threshold = input("Enter memory notification threshold(%): ")
    if threshold.isdigit():
        threshold = int(threshold)
        break
    else:
        print("Enter a number")
while True:
    date = str(datetime.today().date())
    with open(f"{date}-pub.log", 'a') as log:
        log.write("datetime, cpu-usage, number-of-logical-CPUs-used, used-memory, used-disk-space, current-host-ip\n")
        while True:
            log.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, {psutil.cpu_percent(interval)},"
                      + f" {psutil.cpu_count()}, {psutil.virtual_memory().used}, {psutil.disk_usage('C:').used},"
                      + f" {socket.gethostbyname(socket.gethostname())}\n")
            if psutil.virtual_memory().percent > threshold:
                with open(f"{date}-notification.log", 'w') as notification:
                    notification.write("the system is running a low memory")
            sleep(5)
            if str(datetime.today().date()) != date:
                break
