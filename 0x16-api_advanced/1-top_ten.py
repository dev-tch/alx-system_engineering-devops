#!/usr/bin/python3
"""
extract information for api  reddit
"""
import requests


def top_ten(subreddit):
    """return top subredit top 10"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'My-User-Agent'}
    res = requests.get(url, headers=headers)
    if not res.ok:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in res.json().get("data").get("children")]
