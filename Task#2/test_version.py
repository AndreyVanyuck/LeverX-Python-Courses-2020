import unittest
from version import Version

class TestVersion(unittest.TestCase):
    
    def setUp(self):
        self.to_test_eq =  [
            ("1.0.0", "1.0.0"),
            ("1.0.0b", "1.0.0b"),
            ("12.23.0-alpha", "12.23.0-alpha"),
            ("1.2.0-alpha.1", "1.2.0-alpha.1"),
            ("1.0.10-alpha.beta", "1.0.10-alpha.beta"),
            ("1.0.0-rc.1+21AF26D3—-117B344092BD", "1.0.0-rc.1"),
            ("9.2.1+1022", "9.2.1+102"),
            ("9.2.1b", "9.2.1b+102"),
            ("9.2.0", "9.2")
        ]

        self.to_test_lt =  [
            ("1.0.0", "2.0.0"),
            ("1.0.0", "1.42.0"),
            ("1.2.0", "1.2.42"),
            ("1.1.0-alpha", "1.2.0-alpha.1"),
            ("1.0.1b", "1.0.10-alpha.beta"),
            ("1.0.0-rc.1", "1.0.0"),
            ("1.1.3", "2.2.3"),
            ("0.3.0b", "1.2.42"),
            ("1.9.9", "2.1.1"),
            ("1.2.2", "1.3.1"),
            ("1.0.0b", "1.0.1"),
            ("1.0", "1.0.1"),
            ("1.22.2", "2.0.1"),
            ("1.0.9b", "1.1.1"),
            ("9.2.1b", "9.2.1c+102"),
            ("9.2.1", "9.2.1b+102"),
            ("12.23.0-alpha", "12.23.0-alpha.1"), 
            ("1.2.0-alpha.1", "1.2.1-alpha.1"),
            ("1.0.10-alpha.beta", "1.0.10-beta"),
            ("1.0.0-rc.1+21AF26D3—-117B344092BD", "1.0.0-rc.2"),
            ("9.2.1-beta+102", "9.2.1")
        ]


    def test_eq(self):
        for test_case in self.to_test_eq:
            self.assertEqual(Version(test_case[0]), Version(test_case[1]))
    
    def test_not_eq(self):
        for test_case in self.to_test_lt:
            self.assertNotEqual(Version(test_case[0]), Version(test_case[1]))

    def test_lt(self):
        for test_case in self.to_test_lt:
            self.assertLess(Version(test_case[0]), Version(test_case[1])) 
    
    def test_gt(self):
        for test_case in self.to_test_lt:
            self.assertTrue(Version(test_case[1]) > Version(test_case[0]))  
