#!/usr/bin/python3
"""
extract information for api  reddit
"""
import requests


def top_ten(subreddit):
    """return top subredit top 10"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'My-User-Agent'}
    params = {'limit': 10}
    res = requests.get(url, headers=headers,
                       params=params, allow_redirects=False)
    if res.status_code >= 400:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in res.json().get("data").get("children")]
