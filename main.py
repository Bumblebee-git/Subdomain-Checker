import requests
import concurrent.futures
import urllib3

# Suppress insecure request warnings (caused by verify=False)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- Configuration ---
INPUT_FILE = 'subdomains.txt'
OUTPUT_FILE = 'live_subdomains.txt'
TIMEOUT = 5      # Seconds to wait before giving up on a subdomain
THREADS = 20     # Number of subdomains to check simultaneously

def check_subdomain(subdomain):
    """Checks if a subdomain is alive by sending an HTTP and HTTPS request."""
    subdomain = subdomain.strip()
    if not subdomain:
        return None

    # Strip existing protocols if they are already in the file
    if subdomain.startswith(('http://', 'https://')):
        subdomain = subdomain.split('//')[1]

    # Try HTTP first
    try:
        url = f"http://{subdomain}"
        # verify=False ignores SSL errors. allow_redirects follows 301/302 redirects.
        requests.get(url, timeout=TIMEOUT, verify=False, allow_redirects=True)
        return subdomain
    except requests.exceptions.RequestException:
        pass # HTTP failed, let's try HTTPS

    # Try HTTPS if HTTP fails
    try:
        url = f"https://{subdomain}"
        requests.get(url, timeout=TIMEOUT, verify=False, allow_redirects=True)
        return subdomain
    except requests.exceptions.RequestException:
        return None # Both failed, subdomain is considered dead

def main():
    try:
        with open(INPUT_FILE, 'r') as f:
            # Read non-empty lines
            subdomains = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"[-] Error: '{INPUT_FILE}' not found in the current directory.")
        return

    print(f"[*] Loaded {len(subdomains)} subdomains.")
    print(f"[*] Checking for live hosts using {THREADS} threads...\n")
    
    live_subdomains = []

    # Use ThreadPoolExecutor for concurrent checking
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        # Submit all tasks to the executor
        results = executor.map(check_subdomain, subdomains)

        # Process results as they complete
        for result in results:
            if result:
                print(f"[+] Live: {result}")
                live_subdomains.append(result)

    # Save results
    if live_subdomains:
        with open(OUTPUT_FILE, 'w') as f:
            for sub in live_subdomains:
                f.write(f"{sub}\n")
                
        print(f"\n[*] Done! Found {len(live_subdomains)} live subdomains.")
        print(f"[*] Results saved to '{OUTPUT_FILE}'.")
    else:
        print("\n[-] Done! No live subdomains found.")

if __name__ == "__main__":
    main()