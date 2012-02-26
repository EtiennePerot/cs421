"""basic cache util"""

import json
import atexit
from os import path

pjoin = path.join

expiry = 7*24*60*60 # one week in seconds

class Cache(dict):
    """Global Cache dict"""
    filename = None
    def __init__(self, filename=None):
        super(Cache, self).__init__()
        self.filename = filename
        if filename is not None:
            self.init_cache_file()
            atexit.register(self.save_cache_file)
    
    def init_cache_file(self):
        if path.isfile(self.filename):
            with open(self.filename, 'r') as f:
                jdata = f.read()
            if jdata:
                self.update(json.loads(jdata))
    
    def save_cache_file(self):
        with open(self.filename, 'w') as f:
            f.write(json.dumps(dict(self)))
    
    def __repr__(self):
        return "< IMDB Cache %r>"%self.filename
    
    def __str__(self):
        return repr(self)

global_cache = Cache(pjoin(path.expanduser('~'), '.imdb_cache.json'))

        