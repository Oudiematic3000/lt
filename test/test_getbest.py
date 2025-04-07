import unittest
from getbest.getbest import getCols

class TestClass(unittest.TestCase):
    def test_getNumCol(self):
        f=open('test/testdat0.csv', encoding='utf-8')
        _num_col, _mark_col= getCols(f)
        self.assertEqual(_num_col,1)
        f.close()

    def test_getMarkCol(self):
        f=open('test/testdat0.csv', encoding='utf-8')
        _num_col, _mark_col= getCols(f)
        self.assertEqual(_mark_col,4)
        f.close()


if __name__ == '__main__':
    unittest.main()