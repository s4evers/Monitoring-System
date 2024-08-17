import psutil
import time

threshold_percentage = 30
excluded_processes = {'devenv.exe', 'HopToDesk.exe', 'msedge.exe'}

while True:
    for process in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        process_name = process.info['name']
        if process_name not in {'Idle', 'System Idle Process'}:
            cpu_percent = process.info['cpu_percent']
            if cpu_percent > threshold_percentage and process_name not in excluded_processes:
                print(f"High CPU Usage detected in process: {process_name} ({cpu_percent}%)")
    time.sleep(10)
