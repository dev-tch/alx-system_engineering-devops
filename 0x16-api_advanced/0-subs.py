#!/usr/bin/python3
"""
extract information for api  reddit
"""
import requests


def number_of_subscribers(subreddit):
    """return the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
              'User-Agent':
              'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
              }
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code >= 300:
        return 0
    return res.json().get("data").get("subscribers")
