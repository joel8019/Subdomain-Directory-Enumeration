# developed by Joel Hernandez
# 03/10/2022

import requests


def main():
    ans = int(input("What would you like to do today? \n(0) Search for subdomains \n(1) Directory Enumeration \n(2) "
                    "Both\n"))
    domain = ""
    # Subdomain Enumeration
    if ans == 0 or ans == 2:
        subdomains = open("subdomain.txt").read().splitlines()
        domain = input("Please enter the domain name ")
        for s in subdomains:
            url = f"http://{s}.{domain}"
            try:
                requests.get(url)
                print(s)
            except requests.ConnectionError:
                pass
    # Directory Enumeration
    if ans == 1 or ans == 2:
        directories = open("directory.txt").read().splitlines()
        if ans == 1:
            domain = input("Please enter the domain name ")
        for d in directories:
            url = f"http://{domain}/{d}.html"
            request = requests.get(url)
            # If HTML response code is less than 400
            if request.ok:
                print(f"{d} request.status_code")


if __name__ == "__main__":
    main()
