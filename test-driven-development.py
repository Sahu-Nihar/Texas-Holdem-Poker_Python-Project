'''
Test Driven Development (TDD): A process in which the programmer writes tests before writing the code.

Test Driven Development :
# ! (RED) Start -> Write a Test -> Test Fails -> 
# * (GREEN) Write Code to make test pass -> Code pass -> 
# ? (REFACTOR) Workable code how to improve -> Clean code -> Start 
'''

import unittest

def product(a, b):
    return a * b

class TestProduct(unittest.TestCase):
    def test_multiplies_two_number_together(self):
        self.assertEqual(
            product(3,5),
            15
        )

if __name__ == "__main__":
    unittest.main()