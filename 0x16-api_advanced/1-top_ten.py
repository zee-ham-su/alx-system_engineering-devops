#!/usr/bin/python3
"""a function that queries the Reddit API
"""

import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API and
    prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    if not isinstance(subreddit, str):
        return (0)
    user_agent = {
        'User-agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.3'
        )
    }

    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json?limit=10'
    try:
        response = requests.get(url, headers=user_agent)
        response.raise_for_status()
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:
            print("No hot posts found for subreddit '{}'.".format(subreddit))
            return

        for post in posts:
            title = post['data']['title']
            print(title)

    except requests.exceptions.RequestException as req_exc:
        print(None)
