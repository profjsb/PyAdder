__version__ = "0.0.4"
__author__ = "Josh!"

from numpy import array

def run(*args):
    return array(args).sum()

