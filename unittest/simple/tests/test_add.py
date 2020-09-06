import unittest
import playground


class AddTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(playground.add(2, 3), 5)
