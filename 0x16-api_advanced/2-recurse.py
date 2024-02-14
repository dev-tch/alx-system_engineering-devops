#!/usr/bin/python3
"""
extract information for api  reddit
"""
import requests


def recurse(subreddit, hot_list=None, count=0,  after=None):
    """return top subredit top 10"""
    if hot_list is None:
        hot_list = []
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                    AppleWebKit/537.36 (KHTML, like Gecko)\
                    Chrome/58.0.3029.110 Safari/537.3'}

    params = {'count': count, 'after': after}
    res = requests.get(url, headers=headers,
                       params=params, allow_redirects=False)
    if res.status_code >= 400:
        return None
    hot_l = hot_list + [child.get("data").get("title")
                        for child in res.json()
                        .get("data")
                        .get("children")]

    info = res.json()
    if not info.get("data").get("after"):
        return hot_l

    return recurse(subreddit, hot_l, info.get("data").get("count"),
                   info.get("data").get("after"))
