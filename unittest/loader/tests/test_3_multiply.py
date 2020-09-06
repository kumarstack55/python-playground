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


class TestCaseHelper(unittest.TestCase):
    def _get_multiply_obj(self) -> MultiplyBase:
        raise NotImplementedError()

    def test_multiply(self):
        obj: MultiplyBase = self._get_multiply_obj()
        self.assertEqual(obj.multiply(2, 3), 6)


class TestMultiplyBase(TestCaseHelper):
    def _get_multiply_obj(self) -> MultiplyBase:
        return MultiplyBase()

    def test_multiply(self):
        obj: MultiplyBase = self._get_multiply_obj()
        with self.assertRaises(NotImplementedError):
            obj.multiply(2, 3)


class TestMultiplyPlus(TestCaseHelper):
    def _get_multiply_obj(self) -> MultiplyBase:
        return MultiplyPlus()


class TestMultiplyAsterisk(TestCaseHelper):
    def _get_multiply_obj(self) -> MultiplyBase:
        return MultiplyAsterisk()


def load_tests(loader, tests, patterns):
    test_cases = (TestMultiplyBase, TestMultiplyPlus, TestMultiplyAsterisk)
    suite = unittest.TestSuite()
    for test_class in test_cases:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite


if __name__ == '__main__':
    unittest.main()
