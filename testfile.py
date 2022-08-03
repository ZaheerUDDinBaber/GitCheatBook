import requests

def connected_to_internet(url, timeout):
    try:
        _ = requests.head(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("No internet connection available.")
    return False


if connected_to_internet('http://www.google.com/', 5) == True:
    print("Internet Available")
else:        
    print("Internet Not Available")
