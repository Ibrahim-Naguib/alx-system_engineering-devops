#!/usr/bin/python3
"""Queries the Reddit API"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieve the number of subs for a given subreddit from the Reddit API
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 \
                              (by /u/Tiny-Poetry-2335)"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
