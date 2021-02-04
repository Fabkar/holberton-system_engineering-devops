#!/usr/bin/python3
"""
Reddit Api
"""
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts
    listed for a given subreddit."""
    header = {"User-agent": "darth"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=header)
    if response.status_code != 200:
        print("None")
    data = response.json().get('data').get('children')
    for i in data[:9]:
        print(i.get('data').get('title'))
