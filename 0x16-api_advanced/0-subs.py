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
    try:
        res = requests.get(url, headers=headers)
        if res.status_code != 200:
            return 0
        json_obj = res.json()
        item_data = json_obj.get("data", None)
        if item_data is None:
            return 0
        else:
            item_sub = item_data.get("subscribers")
            if item_sub is None:
                return 0
            else:
                return item_sub
    except Exception as e:
        return 0
