#!/usr/bin/python3
""" Recurse it! """
from requests import get


def recurse(subreddit, hot_list=[], after=None, count=0):
    """
    Queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit
    """
    try:
        h = {'User-Agent': 'alx/1.0.0'}
        p = {'limit': 100, 'after': after, 'count': count}
        r = get(
                'https://www.reddit.com/r/{}/hot.json'.format(subreddit),
                headers=h,
                params=p
            )
        after = r.json()['data']['after']
        count += r.json()['data']['dist']
        children = r.json()['data']['children']
        for child in children:
            hot_list.append(child['data']['title'])

        if after is not None:
            recurse(subreddit, hot_list, after, count)

        return hot_list
    except Exception:
        return None
