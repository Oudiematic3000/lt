import unittest
from getbest.getbest import getCols, findTop

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

    def test_findTopID(self):
        f=f=open('test/testdat0.csv', encoding='utf-8')
        _num_col, _mark_col= getCols(f)
        _id, _mark = findTop(f, _num_col, _mark_col)
        self.assertEqual(_id,'167381')
    
    def test_findTopMark(self):
        f=f=open('test/testdat0.csv', encoding='utf-8')
        _num_col, _mark_col= getCols(f)
        _id, _mark = findTop(f, _num_col, _mark_col)
        self.assertEqual(_mark,90)


if __name__ == '__main__':
    unittest.main()