# import subprocess
# import time

# ips = ["8.8.8.8", "1.1.1.1", "192.168.1.1", "10.0.2.15", "256.256.256.256"]

# for ip in ips:
#     print(f"\nPinging {ip}...")
#     start = time.time()

#     try:
#         # Run one ping, ignore output, stop after 1 second
#         result = subprocess.run(
#             ["ping", "-n", "1", ip],
#             stdout=subprocess.DEVNULL,
#             timeout=1
#         )

#         # Calculate ping time
#         elapsed = (time.time() - start) * 1000  # convert to ms

#         if result.returncode == 0:
#             if elapsed <= 500:
#                 print(f"IP {ip} is reachable ({elapsed:.2f} ms)")
#             else:
#                 print(f"IP {ip} is reachable but slow ({elapsed:.2f} ms)")
#         else:
#             print(f"IP {ip} is unreachable")

#     except Exception:
#         print(f"Error pinging {ip}. Trying next IP...")


# import requests

# def fetch_data(url):
#     try:
#         return requests.get(url, timeout=5).json()
#     except Exception as e:
#         print("Error:", e)
#         return None

# for label, url in [
#     ("GOOD", "https://jsonplaceholder.typicode.com/todos/1"),
#     ("BAD", "https://invalid-example-123.com")
# ]:
#     print(f"\nTesting {label} URL:")
#     print(fetch_data(url))





import requests

class APIResponseError(Exception): pass

def fetch(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            raise APIResponseError("Bad status code")
        return r.json()
#     except Exception as e:
#         raise APIResponseError(e)

# for url in [
#     "https://jsonplaceholder.typicode.com/todos/1",
#     "https://wrong-url-12345.com"
# ]:
#     try:
#         print(fetch(url))
#     except APIResponseError as e:
#         print("Error:", e)

import requests
import logging

# Step 1 & 3: Logging setup
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Step 2 & 4: API function with logging
def fetch_data(url):
    logging.info(f"Fetching: {url}")

    try:
        data = requests.get(url, timeout=5).json()
        logging.info("Success")
        return data

    except Exception as e:
        logging.error(f"Error: {e}")
        print("Error:", e)
        return None

# Step 5: Test the function
for label, url in [
    ("GOOD", "https://jsonplaceholder.typicode.com/todos/1"),
    ("BAD", "https://invalid-example-123.com")
]:
    print(f"\nTesting {label} URL:")
    print(fetch_data(url))

