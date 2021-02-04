#!/usr/bin/python3
""" function that queries the Reddit API and returns
the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Method that return the number of subscribers from an Reddit API"""
    header = {"User-agent": "darth"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = (requests.get(url, headers=header))
    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers')
