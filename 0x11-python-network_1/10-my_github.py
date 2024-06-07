#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    username = argv[1]
    pat = argv[2]

    r = requests.get(url, auth=(username, pat))
    try:
        data = r.json().get("id")
        print(data)
    except ValueError:
        print("Not a valid JSON")
        