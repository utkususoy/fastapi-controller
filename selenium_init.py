from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set Chrome options
options = Options()
# options.add_argument("--headless")  # Run in headless mode, optional

# Set up Chrome with webdriver-manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Enable Performance logging
driver.execute_cdp_cmd('Network.enable', {})

# Navigate to the webpage
driver.get("https://www.navaltoday.com/2024/03/04/thales-delivers-first-captas-4-sonar-for-the-us-navys-frigates/")
test = driver.execute_script("var network = performance.getEntries() || {}; return network;")

for item in test:
    print(item)
# Retrieve the network logs
# logs = driver.get_log('performance')
#
# # Process and print network requests
# import json
# for entry in logs:
#     log = json.loads(entry['message'])['message']
#     if log['method'] == 'Network.responseReceived' and 'response' in log['params']:
#         response = log['params']['response']
#         print(f"URL: {response['url']}, Status: {response['status']}")
#
# # Quit the driver
# driver.quit()
