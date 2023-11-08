#!/usr/bin/python3
""" Count it """

import requests


def count_words(subreddit, word_list=[], after=None, hash_words=None):
    """ Queries the Reddit API """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=100'.format(
        subreddit)
    params = {
        'after': after,
    }
    res = requests.get(url, headers={'User-Agent': 'anything'}, params=params,
                       allow_redirects=False)
    if hash_words is None:
        hash_words = {word.lower(): 0 for word in word_list}

    if res.status_code != 200:
        return
    else:
        data = res.json().get('data', {})
        posts = data.get('children', [])
        for post in posts:
            title = (post.get('data', {}).get('title', '')).lower().split()
            for w in title:
                if w in hash_words.keys():
                    hash_words[w] += title.count(w)

        after = data.get('after', None)
        if after:
            return count_words(subreddit, word_list, after, hash_words)
        else:
            word_count = dict(sorted(hash_words.items(),
                                     key=lambda item: (-item[1], item[0])))
            for word, v in word_count.items():
                if v != 0:
                    print(f'{word}: {v}')
