import unittest
import doctest
import sys


def additional_tests():
    import bson
    suite = unittest.TestSuite()
    suite.addTest(doctest.DocTestSuite(bson))
    return suite

def all_tests_suite():
    def get_suite():
        return additional_tests(
            unittest.TestLoader().loadTestsFromNames([
                'adder.tests.test_one_number'
            ]))
    suite = get_suite()
    import adder
    return suite 

def main():
    runner = unittest.TextTestRunner(verbosity=1 + sys.argv.count('-v'))
    suite = all_tests_suite()
    raise SystemExit(not runner.run(suite).wasSuccessful())


if __name__ == '__main__':
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    main()
