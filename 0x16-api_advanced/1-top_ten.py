#!/usr/bin/python3
"""
extract information for api  reddit
"""
import requests


def top_ten(subreddit):
    """return top subredit top 10"""
    url = "https://www.reddit.com/r/{}/top.json?limit=10".format(subreddit)
    headers = {
              'User-Agent':
              'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
              }
    try:
        res = requests.get(url, headers=headers)
        json_obj = res.json()
        item_data = json_obj.get("data", None)
        if item_data is None:
            return 0
        else:
            child_arr = item_data.get("children")
            if child_arr is None:
                return 0
            else:
                for child in child_arr:
                    data2 = child.get("data", None)
                    if data2 is None:
                        continue
                    title = data2.get("title", None)
                    if title is None:
                        continue
                    print(title)
    except Exception as e:
        print("None")
