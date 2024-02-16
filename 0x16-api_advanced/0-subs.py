#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of total subscribers for a given
subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of total subscribers for a
    given subreddit.
    """
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Python/1.0(ALX School 0x16 task 0)'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code >= 400:
        return 0

    return response.json().get('data').get('subscribers')
