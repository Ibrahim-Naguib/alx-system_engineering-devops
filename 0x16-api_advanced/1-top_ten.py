#!/usr/bin/python3
"""Queries the Reddit API"""

import requests


def top_ten(subreddit):
    """
    Retrieve the titles of the first 10 hot posts for a given subreddit

    Parameters:
    - subreddit (str): The name of the subreddit to query.

    Returns:
    - int: The titles of the first 10 hot posts of the specified subreddit or
           None if not a valid subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 \
                              (by /u/Tiny-Poetry-2335)"}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        results = response.json().get("data").get("children")
        [print(result.get("data").get("title")) for result in results]
    else:
        return None
