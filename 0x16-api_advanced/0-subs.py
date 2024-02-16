#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of total subscribers for a given
subreddit.
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of total subscribers for a
    given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Python/1.0(ALX School 0x16 task 0)'}
    response = get(url, headers=headers, allow_redirects=False)
    if not response.ok:
        return 0
    try:
        return response.json().get('data').get('subscribers')
    except Exception:
        return 0
