#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and
displays the body of the response.
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    r = requests.get(argv[1])

    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)
        