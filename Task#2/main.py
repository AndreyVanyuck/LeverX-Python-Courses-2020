import unittest
from test_version import TestVersion


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestVersion)
    unittest.TextTestRunner().run(suite)
