#!/usr/bin/python3
"""
function that queries the Reddit API
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Returns a list containing the titles of all hot
    articles for a given subreddit.
    If no results are found, it returns None.
    """
    user_agent = {
        'User-agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.3'
        )
    }
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    results = requests.get(url, params=parameters, headers=user_agent,
                           allow_redirects=False)

    if results.status_code == 200:
        next_after = results.json().get("data").get("after")
        if next_after is not None:
            recurse(subreddit, hot_list, next_after)

        post_data = results.json().get("data").get("children")
        for post in post_data:
            hot_list.append(post.get("data").get("title"))

        return hot_list
    else:
        return None
