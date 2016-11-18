__version__ = "0.0.1"
__author__ = "Josh!"

from numpy import array

def run(*args):
    return -1*array(args).sum()

