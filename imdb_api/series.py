#!/usr/bin/env python
# encoding: utf-8
"""
Provides functions to interact with the tv_series features of the IMDb iPhone API.
"""

import re

from .movie import ImdbMovie
from .search import search


class ImdbSeries(ImdbMovie):
    
    _seasons = None
    
    def __init__(self, title):
        """Set title ID constant and run the parent's init method.

        Keyword arguments:
        title -- A show's title or imdb id, or even full url

        """
        super(ImdbSeries, self).__init__(title, type='tv_series')
    

    def get_episodes_by_season(self):
        """Get an episode list sorted by season for the current series"""
        arg = {
            "tconst": self.get_title_id()
        }
        if self._seasons is None:
            reply = self.make_request('/title/episodes', arg)
            self._seasons = reply['seasons']
            
        return self._seasons
    
    def __getitem__(self, key):
        for season in self.get_episodes_by_season():
            if season['label'] == 'Season %i'%key:
                return [None] + season['list']
        raise IndexError("No such season: %i"%key)


