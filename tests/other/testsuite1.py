# -*- coding: utf-8 -*-

import unittest
from waits import WaitForElements
from assertions import Assertsions


class Testsuite1(unittest.TestSuite):

    def suite(self):
        suite = unittest.TestSuite()
        suite.addTest(WaitForElements())
        suite.addTest(Assertsions())
        return suite

if __name__ == '__main__':
    unittest.main()