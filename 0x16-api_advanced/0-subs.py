#!/usr/bin/python3
""" How many subs? """
from requests import get


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    """
    try:
        h = {'User-Agent': 'alx/1.0.0'}
        r = get(
                'https://www.reddit.com/r/{}/about.json'.format(subreddit),
                headers=h
            )
        subscribers = r.json()['data']['subscribers']
        return subscribers
    except Exception:
        return 0
