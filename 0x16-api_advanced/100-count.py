#!/usr/bin/python3
"""function that queries the Reddit API"""

import requests


def count_words(subreddit, word_list, after="", word_cnts=None):
    """Count occurrences of words in subreddit titles"""

    if after == "":
        word_cnts = {word.lower(): 0 for word in word_list}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after}
    headers = {'user-agent': 'bhalut'}

    response = requests.get(url, params=params,
                            allow_redirects=False, headers=headers)

    if response.status_code == 200:
        data = response.json()

        for post in data['data']['children']:
            for word in post['data']['title'].split():
                word_lower = word.lower()
                if word_lower in word_cnts:
                    word_cnts[word_lower] += 1

        next_after = data['data']['after']

        if next_after is None:
            save = set()
            for i, word1 in enumerate(word_list):
                for j, word2 in enumerate(word_list[i+1:], start=i+1):
                    if word1.lower() == word2.lower():
                        save.add(j)
                        word_cnts[word1.lower()] += word_cnts[word2.lower()]

            sorted_word_counts = sorted(word_cnts.items(),
                                        key=lambda x: (-x[1], x[0]))

            for word, count in sorted_word_counts:
                if count > 0 and word not in save:
                    print("{}: {}".format(word, count))
        else:
            count_words(subreddit, word_list, next_after, word_cnts)
