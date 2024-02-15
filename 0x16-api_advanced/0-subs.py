#!/usr/bin/python3
"""extract information for api  reddit"""


def number_of_subscribers(subreddit):
    """return the number of subscribers"""
    import requests

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My-User-Agent'}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    return res.json().get('data').get('subscribers')
