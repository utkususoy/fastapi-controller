# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# import json

# # Function to print the URLs of the network requests
# # def print_network_requests(driver):
# #     logs = driver.get_log('performance')
# #     for entry in logs:
# #         log = json.loads(entry['message'])['message']
# #         if 'Network.requestWillBeSent' in log['method']:
# #             request = log['params']['request']
# #             if 'image' in request['url']:
# #                 print('Image URL Requested:', request['url'])

# # # Set up Chrome options to enable logging
# # Setup Chrome options
# chrome_options = webdriver.ChromeOptions()
# # chrome_options.add_argument("--remote-debugging-port=9222")  # This is important for DevTools
# chrome_options.add_argument("--headless")  # Enable headless mode
# chrome_options.add_argument("--window-size=1920,10000")
# # chrome_options.add_experimental_option('w3c', False)
# # chrome_options.add_experimental_option('perfLoggingPrefs', {'enableNetwork': True})
# # chrome_options.add_argument("--enable-logging")
# # chrome_options.add_argument("--log-level=0")

# # Set up driver with the path to Chromedriver
# service = ChromeService(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=chrome_options)

# # Enable Performance Logging via CDP to monitor network operations
# driver.execute_cdp_cmd("Network.enable", {})

# # Navigate to a webpage
# driver.get("https://westwardshippingnews.com/1-3-million-overhaul-of-millbay-docks/")
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# import json

# # Function to print the URLs of the network requests
# # def print_network_requests(driver):
# #     logs = driver.get_log('performance')
# #     for entry in logs:
# #         log = json.loads(entry['message'])['message']
# #         if 'Network.requestWillBeSent' in log['method']:
# #             request = log['params']['request']
# #             if 'image' in request['url']:
# #                 print('Image URL Requested:', request['url'])

# # # Set up Chrome options to enable logging
# # Setup Chrome options
# chrome_options = webdriver.ChromeOptions()
# # chrome_options.add_argument("--remote-debugging-port=9222")  # This is important for DevTools
# chrome_options.add_argument("--headless")  # Enable headless mode
# chrome_options.add_argument("--window-size=1920,10000")
# # chrome_options.add_experimental_option('w3c', False)
# # chrome_options.add_experimental_option('perfLoggingPrefs', {'enableNetwork': True})
# # chrome_options.add_argument("--enable-logging")
# # chrome_options.add_argument("--log-level=0")

# # Set up driver with the path to Chromedriver
# service = ChromeService(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=chrome_options)

# # Enable Performance Logging via CDP to monitor network operations
# driver.execute_cdp_cmd("Network.enable", {})

# # Navigate to a webpage
# driver.get("https://westwardshippingnews.com/1-3-million-overhaul-of-millbay-docks/")

# # Wait until the body tag is present
# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.TAG_NAME, "body"))
# )

# script_to_inject = """
# return window.performance.getEntriesByType('resource').filter((resource) => {
#     return resource.initiatorType === 'img';
# }).map((imageResource) => {
#     return {
#         url: imageResource.name,
#         duration: imageResource.duration.toFixed(2),
#         startTime: imageResource.startTime.toFixed(2),
#         endTime: (imageResource.startTime + imageResource.duration).toFixed(2)
#     };
# });
# """

# # Execute the script and capture the result
# image_load_data = driver.execute_script(script_to_inject)

# # Print or process the image load data
# for image in image_load_data:
#     print(f"Image URL: {image['url']}, Load Duration: {image['duration']}ms, Start Time: {image['startTime']}ms, End Time: {image['endTime']}ms")

# # Close the browser
# driver.quit()


# # Wait until the body tag is present
# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.TAG_NAME, "body"))
# )

# script_to_inject = """
# return window.performance.getEntriesByType('resource').filter((resource) => {
#     return resource.initiatorType === 'img';
# }).map((imageResource) => {
#     return {
#         url: imageResource.name,
#         duration: imageResource.duration.toFixed(2),
#         startTime: imageResource.startTime.toFixed(2),
#         endTime: (imageResource.startTime + imageResource.duration).toFixed(2)
#     };
# });
# """

# # Execute the script and capture the result
# image_load_data = driver.execute_script(script_to_inject)

# # Print or process the image load data
# for image in image_load_data:
#     print(f"Image URL: {image['url']}, Load Duration: {image['duration']}ms, Start Time: {image['startTime']}ms, End Time: {image['endTime']}ms")

# # Close the browser
# driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Set Chrome options
options = Options()
options.add_argument("--headless")  # Run in headless mode, optional
# chrome_options.add_argument("--headless")  # Enable headless mode
options.add_argument("--window-size=1920,10000")
# Set up Chrome with webdriver-manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Enable Performance logging
driver.execute_cdp_cmd('Network.enable', {})

# Navigate to the webpage
# driver.get("https://www.navaltoday.com/2024/03/04/thales-delivers-first-captas-4-sonar-for-the-us-navys-frigates/")
test = driver.execute_script("var network = performance.getEntries() || {}; return network;")

# # Navigate to a webpage
# driver.get("https://westwardshippingnews.com/1-3-million-overhaul-of-millbay-docks/")
driver.get("https://www.navaltoday.com/2024/03/08/austal-delivers-new-guardian-class-patrol-boat-to-australia-2/")

# Wait until the body tag is present
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "body"))
)


import time
time.sleep(10)
image_load_data = []
# while True:
#     if len(image_load_data) >= len(imgs):
#         break
located_images = driver.find_elements(By.TAG_NAME, "img")
# try:
loaded_images = []
timer = 0
while True:
    # Retrieve all image elements from the webpage
    print(len(located_images))
    time.sleep(1)
    if timer > 5:
        break
    # Apply the JavaScript function to each image element and check if it has loaded
    for img in located_images:
        
        
        # Construct the JavaScript command to apply the function
        js_command = """
        function isImageVisible(imgElement) {
            // Check if the image has loaded
            const hasLoaded = imgElement.complete && imgElement.naturalHeight !== 0;

            // Get computed style to check visibility and display properties
            const style = window.getComputedStyle(imgElement);
            const isVisible = style.display !== 'none' && style.visibility !== 'hidden' && style.opacity > 0;

            // Check if the image is within the viewport
            const rect = imgElement.getBoundingClientRect();
            const isInViewport = rect.top < window.innerHeight && rect.left < window.innerWidth && rect.bottom > 0 && rect.right > 0;

            return hasLoaded && isVisible && isInViewport;
        }
        return isImageVisible(arguments[0]);
        """
        # imgElement.complete && imgElement.naturalHeight !== 0
        # Execute the command and print the result
        is_loaded = driver.execute_script(js_command, img)
        # print(f"{is_loaded}, src: {img.get_attribute('src')}")
        if is_loaded:
            loaded_images.append(img.get_attribute('src'))
            located_images.remove(img)
    timer += 1

print(len(loaded_images))
for load_img in loaded_images:
    print(load_img)
# except:
#     print("no src.")
    
# script_to_inject = """
#     return window.performance.getEntriesByType('resource').filter((resource) => {
#         return resource.initiatorType === 'img';
#     }).map((imageResource) => {
#         return {
#             url: imageResource.name,
#             duration: imageResource.duration.toFixed(2),
#             startTime: imageResource.startTime.toFixed(2),
#             endTime: (imageResource.startTime + imageResource.duration).toFixed(2)
#         };
#     });
#     """

# # Execute the script and capture the result
# image_load_data = driver.execute_script(script_to_inject)


# # Print or process the image load data
# for image in image_load_data:
#     print(f"Image URL: {image['url']}, Load Duration: {image['duration']}ms, Start Time: {image['startTime']}ms, End Time: {image['endTime']}ms")

# # print(test)
# print("end")
