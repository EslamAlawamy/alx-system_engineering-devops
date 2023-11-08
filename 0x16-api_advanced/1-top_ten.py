#!/usr/bin/python3
""" Top Ten """
from requests import get


def top_ten(subreddit):
    """
    queries the Reddit API and prints the titles of the first 10 hot posts
    """
    try:
        h = {'User-Agent': 'alx/1.0.0'}
        p = {'limit': 10}
        r = get(
                'https://www.reddit.com/r/{}/hot.json'.format(subreddit),
                headers=h,
                params=p
            )
        children = r.json()['data']['children']
        for child in children:
            print(child['data']['title'])
    except Exception:
        print(None)
