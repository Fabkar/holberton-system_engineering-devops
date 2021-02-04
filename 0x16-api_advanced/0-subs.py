#!/usr/bin/pyhton3
""" function that queries the Reddit API and returns
the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Method that return the number of subscribers from an Reddit API"""
    header = {"User-agent": "darth"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = (requests.get(url, headers=header))
    try:
        result = response.json().get('data').get('subscribers')
        if result is None:
            raise TypeError
        return response.json().get('data').get('subscribers')
    except Exception:
        return 0
