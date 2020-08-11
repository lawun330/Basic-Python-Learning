#!/usr/bin/env python3

'''Automated Testing : unit testing'''

from email_change_script import contains_domain
import unittest

class TestContainsDomain(unittest.TestCase):
    def test_basic(self):
        address = 'happy_coder@gmail.com'
        domain = 'gmail.com'
        expected = True
        self.assertEqual(contains_domain(address,domain),expected)
    def test_none_domain(self):
        address = 'happy_coder@gmail.com'
        domain   = ''
        expected = 'NameError: Please insert the domain'
        self.assertEqual(contains_domain(address,domain),expected)
unittest.main()

"""
MORE at
'https://docs.python.org/3/library/unittest.html#basic-example',
'https://docs.python.org/3/library/unittest.html#command-line-interface',
'https://docs.python.org/3/library/unittest.html#organizing-test-code'
"""

#Testing methods
'''
-unit test : To verify a small part (isolated) of the code is correct
-integration test : It verifies that different parts of the overall system interact as expected
-smoke test : A sanity check to find major bugs in a program
-load test : To ensure the code behave well under significantly stressed testing conditions
-regression test : A test where a bug has been identified in order to ensure the same bug doesn't show up again later
-black-box test : Tester has no knowledge of the code, thus unbiased
-white-box test : Testing begins after the code is developed
'''
