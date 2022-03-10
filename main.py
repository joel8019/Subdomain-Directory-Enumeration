# developed by Joel Hernandez
# 03/10/2022

import requests


def main():

    ans = input("What would you like to do today? \n(0) Search for subdomains \n(1) Directory Enumeration \n(2) Both\n")
    print(ans)
    subdomains = open("file.txt").read().splitlines()
    domain = input("Please enter the domain name ")
    if ans == 0 or ans == 2:
        for s in subdomains:
            url = f"http://{s}.{domain}"
            try:
                requests.get(url)
                print(s)
            except requests.ConnectionError:
                pass
    if ans == 1 or ans ==2:



if __name__ == "__main__":
    main()
