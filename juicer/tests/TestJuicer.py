#!/usr/bin/env python
import unittest
from juicer.juicer.Juicer import Juicer as j
from juicer.juicer.Parser import Parser as pmoney
from juicer.utils import mute


class TestJuicer(unittest.TestCase):

    def setUp(self):
        self.parser = pmoney()

    def test_rpm_search(self):
        self.args = self.parser.parser.parse_args('rpm-search ruby'.split())
        pulp = j(self.args)
        output = mute()(pulp.search_rpm)(name=self.args.rpmname)

        self.args = self.parser.parser.parse_args(\
            'rpm-search ruby --in qa'.split())
        pulp = j(self.args)
        output = mute()(pulp.search_rpm)(name=self.args.rpmname)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestJuicer)
    unittest.TextTestRunner(verbosity=2).run(suite)
