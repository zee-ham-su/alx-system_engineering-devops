#!/usr/bin/python3
"""
function that queries the Reddit API
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursive function that queries the Reddit API, parses the titles
    of all hot articles, and prints a sorted count of given keywords.
    """
    if counts is None:
        counts = {}

    user_agent = {
        'User-agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.3'
        )
    }

    url = 'https://www.reddit.com/r/{}/hot.json?limit=100'.format(subreddit)
    if after:
        url += '&after={}'.format(after)

    try:
        response = requests.get(url, headers=user_agent)
        response.raise_for_status()
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        for post in posts:
            title = post['data']['title'].lower()

            for word in word_list:
                if title.count(word.lower()):
                    counts[word.lower()] = counts.get(word.lower(), 0) + \
                       title.count(word.lower())

        next_after = data.get('data', {}).get('after')
        if next_after:
            count_words(subreddit, word_list, next_after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

            for word, count in sorted_counts:
                print('{}: {}'.format(word, count))

    except requests.exceptions.RequestException as req_exc:
        print('Error: {}'.format(req_exc))
