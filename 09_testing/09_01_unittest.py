'''
Demonstrate your knowledge of unittest by first creating a function with input parameters and a return value.

Once you have a function, write at least two tests for the function that use various assertions. The
test should pass.

Also include a test that does not pass.

'''

import unittest

#area of a paper
def area_paper(a):
    return a ** 2


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(area_paper(2), 3)

class MyTest_2(unittest.TestCase):
    def test(self):
        self.assertEqual(area_paper(4),16)

class MyTest_3(unittest.TestCase):
    def test(self):
        self.assertEqual(area_paper(4),15)
