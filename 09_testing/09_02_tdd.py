'''
Write a script that demonstrates TDD. Using pseudocode, plan out a couple simple functions. They could be
as simple as add and subtract or more complex such as functions that read and write to files.

Instead of writing out the functions, only provide the tests. Think about how the functions might
fail and write tests that will check and prevent failure.

You do not need to implement the actual functions after writing the tests but you may.

'''
import math
import unittest

def hello_world():
    return 'hello world'

class Test1(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_world(), "hello world")

def circumfence_circle(x):
    return 2 * x * math.pi


class Test2(unittest.TestCase):
    def test_circumfence(self):
        self.assertEqual(circumfence_circle(1), 6.283185307179586)
