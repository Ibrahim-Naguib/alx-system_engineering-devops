#!/usr/bin/python3
"""Queries the Reddit API"""

import requests


def count_words(subreddit, word_list, found_words=[], after=None):
    """
    Recursively retrieves hot posts from a subreddit.

    Parameters:
    - subreddit (str): The name of the subreddit.
    - hot_list (list): A list to store the titles of hot articles.
    - after (str): A parameter used for pagination.

    Returns:
    - A list of titles of hot articles from the subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 \
                              (by /u/Tiny-Poetry-2335)"}
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if after is None:
        word_list = [word.lower() for word in word_list]

    if response.status_code == 200:
        results = response.json().get("data")
        after = results.get("after")
        for result in results.get("children"):
            title = result.get("data").get("title").lower()
            for word in title.split(" "):
                if word in word_list:
                    found_words.append(word)

        if after is not None:
            return count_words(subreddit, word_list, found_words, after)
        else:
            result = {}
            for word in found_words:
                if word.lower() in result.keys():
                    result[word.lower()] += 1
                else:
                    result[word.lower()] = 1
            for key, value in sorted(result.items(), key=lambda item: item[1],
                                     reverse=True):
                print("{}: {}".format(key, value))
    else:
        return
