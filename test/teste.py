import unittest
from sub_pack.lib import add

class TestSoma(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(add(2,3),5, "Deveria ser 5")

if __name__ == '__main__':
    unittest.main()
