import psutil
import logging
import time

# Configure logging
logging.basicConfig(filename="system_health.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Thresholds 
CPU_THRESHOLD = 80.0  # in percentage
MEMORY_THRESHOLD = 80.0  # in percentage
DISK_THRESHOLD = 80.0  # in percentage

# Function to monitor system health
def monitor_system_health():
    try:
        # Check CPU usage
        cpu_usage = psutil.cpu_percent(interval=1)
        if cpu_usage > CPU_THRESHOLD:
            logging.warning(f"High CPU Usage: {cpu_usage}%")
            print(f"Alert: High CPU Usage - {cpu_usage}%")

        # Check Memory usage
        memory = psutil.virtual_memory()
        memory_usage = memory.percent
        if memory_usage > MEMORY_THRESHOLD:
            logging.warning(f"High Memory Usage: {memory_usage}%")
            print(f"Alert: High Memory Usage - {memory_usage}%")

        # Check Disk usage
        disk = psutil.disk_usage('/')
        disk_usage = disk.percent
        if disk_usage > DISK_THRESHOLD:
            logging.warning(f"High Disk Usage: {disk_usage}%")
            print(f"Alert: High Disk Usage - {disk_usage}%")

        # Check running processes
        process_count = len(psutil.pids())
        logging.info(f"Number of running processes: {process_count}")
        print(f"Running processes: {process_count}")

    except Exception as e:
        logging.error(f"Error occurred while monitoring system health: {e}")
        print(f"Error: {e}")

# Main function to monitor system health every 60 seconds
if __name__ == "__main__":
    print("Starting System Health Monitoring...")
    while True:
        monitor_system_health()
        time.sleep(60)  # Check every 60 seconds
