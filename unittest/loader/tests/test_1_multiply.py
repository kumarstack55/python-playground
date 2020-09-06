#!/usr/bin/env python
import unittest


class MultiplyBase(object):
    def multiply(self, n1: int, n2: int) -> int:
        raise NotImplementedError()


class MultiplyPlus(MultiplyBase):
    def multiply(self, n1: int, n2: int) -> int:
        ret = 0
        for i in range(0, n1):
            ret += n2
        return ret


class MultiplyAsterisk(MultiplyBase):
    def multiply(self, n1: int, n2: int) -> int:
        return n1 * n2


class TestMultiplyBase(unittest.TestCase):
    def test_multiply(self):
        obj: MultiplyBase = MultiplyBase()
        with self.assertRaises(NotImplementedError):
            obj.multiply(2, 3)


class TestMultiplyPlus(unittest.TestCase):
    def test_multiply(self):
        obj: MultiplyBase = MultiplyPlus()
        self.assertEqual(obj.multiply(2, 3), 6)  # 冗長!!


class TestMultiplyAsteriskClass(unittest.TestCase):
    def test_multiply(self):
        obj: MultiplyBase = MultiplyAsterisk()
        self.assertEqual(obj.multiply(2, 3), 6)  # 冗長!!


#def load_tests(loader, tests, patterns):
#    test_cases = (MyTestCase,)
#    suite = unittest.TestSuite()
#    for test_class in test_cases:
#        tests = loader.loadTestsFromTestCase(test_class)
#        suite.addTests(tests)
#    return suite

if __name__ == '__main__':
    unittest.main()
