#!/usr/bin/env python
# encoding: utf-8
"""
search.py

Provides functions to interact with the search feature of the IMDb iPhone API.
"""

from __future__ import absolute_import

import urllib

from .base import instance

def search(term, extra=None):
    i = instance()

    arg = {"q": term}
    if extra:
        arg.update(extra)
    result_list = i.make_request('/find', arg)['results']
    results = {}
    for r in result_list:
        results[r['label']] = r['list']
    return results

def title_search(term, extra=None):
    res = search(term, extra=extra)
    for key in res.keys():
        if 'Title' not in key:
            del res[key]
    return res
        
def name_search(term, extra=None):
    """Search names only"""
    res = search(term, extra=extra)
    for key in res.keys():
        if 'Name' not in key:
            del res[key]
    return res
