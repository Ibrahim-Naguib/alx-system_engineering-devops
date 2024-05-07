#!/usr/bin/python3
"""Queries the Reddit API"""

import requests


def recurse(subreddit, hot_list=[], after=None):
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

    if response.status_code == 404:
        return None
    results = response.json().get("data")
    after = results.get("after")
    for result in results.get("children"):
        hot_list.append(result.get("data").get("title"))
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
