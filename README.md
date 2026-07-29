# Subdomain-Checker
A fast, concurrent Python tool for verifying live subdomains. Essential for bug bounty recon and penetration testing.


Install the required dependencies:

Bash
pip install requests
Usage
Create a file named subdomains.txt in the same directory as the script.

Add your list of subdomains to subdomains.txt (one per line).

Run the script:

Bash
python main.py
The script will output the live subdomains to the console and save them to live_subdomains.txt.

Configuration
You can easily adjust the script's behavior by modifying the variables at the top of the file:

INPUT_FILE: Name of the file containing subdomains to check (default: subdomains.txt)

OUTPUT_FILE: Name of the file to save live subdomains (default: live_subdomains.txt)

TIMEOUT: Seconds to wait before giving up on a host (default: 5)

THREADS: Number of subdomains to check concurrently (default: 20)
