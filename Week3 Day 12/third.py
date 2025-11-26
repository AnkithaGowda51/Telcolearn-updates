import requests
import logging
logging.basicConfig(filename='log.txt',level=logging. WARNING)
logging.info('info information')
logging.debug('debug information')
logging.warning('warningi information')
def fetch_data(url):
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        return r.json()
    except requests.RequestException as e:
        print("Request error:", e)
    except ValueError:
        print("Invalid JSON response.")
    return None

def main():
    for label, url in (("GOOD", "https://jsonplaceholder.typicode.com/todos/1"),
                       ("BAD", "https://invalid-example-123.com")):
        print(f"\nTesting {label} URL:")
        print(fetch_data(url))

if __name__ == "__main__":
    main()