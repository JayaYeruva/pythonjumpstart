#!/usr/bin/env python

import unittest

import unittest1
import unittest2
import unittest3

loader = unittest.TestLoader()

suite = loader.loadTestsFromModule(unittest1)
suite.addTests(loader.loadTestsFromModule(unittest2))
suite.addTests(loader.loadTestsFromModule(unittest3))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
