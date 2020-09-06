import unittest


def add(x, y):
    return x + y


class MyTestCaseBase(unittest.TestCase):
    def test_add(self):
        self.assertTrue(False)


class MyTestCase(MyTestCaseBase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)


def load_tests(loader, tests, patterns):
    test_cases = (MyTestCase,)
    suite = unittest.TestSuite()
    for test_class in test_cases:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite
