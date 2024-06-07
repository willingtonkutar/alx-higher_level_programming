#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status

- You must use the package requests
- You are not allow to import packages other than requests
- The body of the response must be display like the following
(tabulation before -)
"""
import requests
r = requests.get('https://alx-intranet.hbtn.io/status')
text = r.text
print("Body response:")
print(f"\t- type: {type(text)}")
print(f"\t- content: {text}")
