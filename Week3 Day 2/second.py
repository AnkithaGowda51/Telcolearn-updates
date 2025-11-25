import requests

def fetch_data(url):
    try:
        response = requests.get(url, timeout=5)   # API request with timeout
        response.raise_for_status()               # Handles 4xx & 5xx errors
        return response.json()                    # Convert JSON to Python dict

    except requests.exceptions.Timeout:
        print("Error: Request timed out.")
    except requests.exceptions.ConnectionError:
        print("Error: Cannot reach the server (host unreachable).")
    except requests.exceptions.HTTPError as e:
        print("Error: Bad status code:", e.response.status_code)
    except ValueError:
        print("Error: Invalid or Non-JSON response.")
    except Exception as e:
        print("Unexpected Error:", e)

    return None


def main():
    good_url = "https://jsonplaceholder.typicode.com/todos/1"
    bad_url = "https://invalid-example-123.com"

    print("\nTesting GOOD URL:")
    print(fetch_data(good_url))

    print("\nTesting BAD URL:")
    print(fetch_data(bad_url))


if __name__ == "__main__":
    main()
import requests

def fetch_data(url):
    try:
        response = requests.get(url, timeout=5)   # API request with timeout
        response.raise_for_status()               # Handles 4xx & 5xx errors
        return response.json()                    # Convert JSON to Python dict

    except requests.exceptions.Timeout:
        print("Error: Request timed out.")
    except requests.exceptions.ConnectionError:
        print("Error: Cannot reach the server (host unreachable).")
    except requests.exceptions.HTTPError as e:
        print("Error: Bad status code:", e.response.status_code)
    except ValueError:
        print("Error: Invalid or Non-JSON response.")
    except Exception as e:
        print("Unexpected Error:", e)

    return None


def main():
    good_url = "https://jsonplaceholder.typicode.com/todos/1"
    bad_url = "https://invalid-example-123.com"

    print("\nTesting GOOD URL:")
    print(fetch_data(good_url))

    print("\nTesting BAD URL:")
    print(fetch_data(bad_url))


if __name__ == "__main__":
    main()
