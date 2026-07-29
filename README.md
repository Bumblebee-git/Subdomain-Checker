# Subdomain-Checker


A fast, concurrent Python script to verify live subdomains from a given list. Essential for bug bounty reconnaissance and penetration testing.

## Features
- **Fast & Concurrent:** Uses Python's `ThreadPoolExecutor` to check multiple subdomains simultaneously.
- **Smart Protocol Handling:** Automatically attempts HTTP first, and falls back to HTTPS if HTTP fails.
- **Clean Input Parsing:** Automatically strips `http://` or `https://` from the input file if present.
- **Clean Output:** Saves only the active, reachable subdomains to a new text file.
- **Error Tolerant:** Ignores SSL errors (`verify=False`), follows redirects, and suppresses insecure request warnings to keep terminal output clean.

## Prerequisites
- Python 3.6+
- `requests` library


