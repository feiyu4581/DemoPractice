from native import match as native_match
from rabin_karp import match as rabin_karp_match
from automation import match as automation_match
from kmp import match as kmp_match
import unittest
from collections import namedtuple

match = namedtuple('Match', 'text pattern res')

MATCH_DATA = [
    match('ABIDANCE', 'DAN', [3]),
    match('bcabababaababacabab', 'ababaca', [9]),
    match('AFD213dfsD2', 'D2', [2, 9]),
    match('你们很好吗，我们很好', '好', [3, 9])
]

MATCH_METHODS = [
    native_match,
    rabin_karp_match,
    automation_match,
    kmp_match
]


class TestStringMatcher(unittest.TestCase):
    def setUp(self):
        super()

        self.match_method = match

    def test_match(self):
        for data in MATCH_DATA:
            for method in MATCH_METHODS:
                self.assertEqual(method(data.text, data.pattern), data.res)


if __name__ == '__main__':
    unittest.main()