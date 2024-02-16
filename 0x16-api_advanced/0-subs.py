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
    headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                    AppleWebKit/537.36 (KHTML, like Gecko)\
                    Chrome/58.0.3029.110 Safari/537.3'}
    response = get(url, headers=headers, allow_redirects=False)
    if not response.ok:
        return 0
    try:
        return response.json().get('data').get('subscribers')
    except Exception:
        return 0
