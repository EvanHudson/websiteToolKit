import requests
import time
#https://www.stationx.net/python-hacking-tools/
#buffer overflow by entering long strings and negatives in text entry boxes
#sql injections
#https://github.com/digininja/DVWA
def fetch_page(url):
    """Fetches the content of a webpage and returns True if successful, False otherwise."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        print(f"Checking URL: {url} | Status: {response.status_code}")
        #time.sleep(1)  # Adding a delay between requests
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return False

# Load dictionary words into a list (avoid multiple file reads)
dictionary_path = "test.txt"  # Replace with the correct path
#dictionary_path = "dictionary.txt"
with open(dictionary_path, 'r') as file:
    wordlist = [line.strip() for line in file]

base_url = input("Enter website: ")
base_url=f"https://www.{base_url}/"
#base_url=f"https://{base_url}/"
found_paths = set()  # Use a set to track discovered paths
queue = [""]  # Start from the base URL

while queue:
    current_path = queue.pop(0)  # Process the first path in the queue
    new_paths_found = False  # Track if any new paths are found

    for word in wordlist:
        new_path = f"{current_path}{word}/"
        full_url = f"{base_url}{new_path}"

        if fetch_page(full_url):
            print(f"✅ Found: {full_url}")
            if new_path not in found_paths:
                found_paths.add(new_path)
                queue.append(new_path)  # Add new path to queue for deeper exploration
                new_paths_found = True  # Mark that a new path was found

    # If no new paths were found at this level, we consider it fully explored
    if not new_paths_found:
        print(f"🔍 Completed search for: {base_url}{current_path}")

# Print all discovered paths
print("\n🎯 Discovered Paths:")
for path in found_paths:
    print(f"{base_url}{path}")
