import requests
import logging
import time

# Configure logging
logging.basicConfig(filename="application_health.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Application URL
APP_URL = "http://example.com"  # Replace with the actual application URL

def check_application_health():
    try:
        response = requests.get(APP_URL, timeout=5)
        if response.status_code == 200:
            logging.info(f"Application is UP. Status code: {response.status_code}")
        else:
            logging.warning(f"Application is DOWN. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Application is DOWN. Error: {e}")

if __name__ == "__main__":
    while True:
        check_application_health()
        time.sleep(60)  # Check every 60 seconds
