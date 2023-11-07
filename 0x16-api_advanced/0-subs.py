#!/usr/bin/python3
"""
the number of subscribers (not active users, total subscribers)
for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and returns
    the number of subscribers (not active users,
    total subscribers) for a given subreddit.
    """
    if not isinstance(subreddit, str):
        return (0)

    user_agent = {
        'User-agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.3'
        )
    }

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    try:
        response = requests.get(url, headers=user_agent)
        response.raise_for_status()
        results = response.json()
        return results.get('data', {}).get('subscribers', 0)

    except requests.exceptions.RequestException as req_exc:
        return (0)
