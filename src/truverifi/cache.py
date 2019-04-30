import os, os.path as osp

import truverifi
from   truverifi.util.system import makedirs

class Cache:
    def __init__(self, location = None, dirname = None):
        self.location = location or osp.expanduser("~")
        self.dirname  = dirname  or ".%s" % (truverifi.__name__)

    def create(self, exist_ok = True):
        path = osp.join(self.location, self.dirname)
        makedirs(path, exist_ok = exist_ok)