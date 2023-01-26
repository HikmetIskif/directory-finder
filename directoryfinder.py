#!/usr/bin/env python3
import urllib.request
import sys

def directory_bust(url, wordlist):
    with open(wordlist, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            path = line.strip()
            req = urllib.request.Request(url + '/' + path)
            try:
                with urllib.request.urlopen(req) as response:
                    if response.code != 404:
                        print(f"[+] Found: {url}/{path}", file=sys.stdout)
            except KeyboardInterrupt:
            	print("Keyboard interrupt detected, exiting..")
            	sys.exit()
            except:
                pass

# Example usage:
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('usage: python script.py <url> <wordlist>', file=sys.stderr)
        sys.exit(1)
    url = sys.argv[1]
    wordlist = sys.argv[2]
    directory_bust(url, wordlist)
