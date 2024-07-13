import requests
import time

def download_urls(urls):
    results = {}
    for url in urls:
        attempts = 0
        while attempts < 3:
            try:
                response = requests.get(url)
                response.raise_for_status()  
                results[url] = response.text
                break
            except requests.exceptions.RequestException as e:
                print(f"Error downloading {url}: {e}")
                attempts += 1
                time.sleep(1)  # Wait 1 second before retrying
        if attempts == 3:
            results[url] = f"Failed to download {url} after 3 attempts"
    return results

# Example usage:
urls = [
    "https://www.example.com",
    "https://www.google.com",
    "https://invalid-url.com",  # This URL will raise an exception
    "https://www.python.org"
]

results = download_urls(urls)
for url, content in results.items():
    print(f"URL: {url}, Content: {content[:50]}...")