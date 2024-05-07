#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Retrieve the number of subs"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        results = response.json()
        return results["data"]["subscribers"]
    else:
        return 0
