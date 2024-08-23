#!/usr/bin/env python3

''' ### Automated Testing : Unit Testing ###

This script is a basic example of how to use the unittest module in Python.

There are many types of testing methods in Python:
* Unit test: Checks if a small, isolated part of the code works correctly.
* Integration test: Ensures different parts of the system work together as expected.
* Smoke test: A sanity check to find major bugs in a program.
* Load test: Checks if the code performs well under heavy usage (significantly stressed testing conditions).
* Regression test: Ensures a bug that was fixed doesn't appear again.
* Black-box test: Tester has no knowledge of the code, ensuring unbiased testing.
* White-box test: Testing is done with knowledge of the code after it is developed.

For more information, please visit
>>> https://docs.python.org/3/library/unittest.html#basic-example,
>>> https://docs.python.org/3/library/unittest.html#command-line-interface,
>>> https://docs.python.org/3/library/unittest.html#organizing-test-code. '''

########################################################################################

import unittest
from change_email_domain import contains_domain

class TestContainsDomain(unittest.TestCase):
    def test_basic(self):
        address = 'happy_coder@gmail.com'
        domain = 'gmail.com'
        expected = True
        self.assertEqual(contains_domain(address, domain), expected)


    def test_none_domain(self):
        address = 'happy_coder@gmail.com'
        domain   = ''
        expected = 'NameError: Please insert the domain'
        self.assertEqual(contains_domain(address, domain), expected)


unittest.main()
