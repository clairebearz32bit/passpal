import os
import random

from string import ascii_lowercase as lower
from passpal import PERMUTATIONS

class PassPal:
    def __init__(self, pass_len, max_len=128, min_len=8):
        """
        This class is the main object to generate a strong and secure password,
        along with a phrase to help remember it.
        """

        assert(pass_len < max_len or pass_len > min_len), 'Password must be between 8 and 128 characters long.'

        try:
            self.pass_len = pass_len

        except AssertionError as e:
            print(e)


    def generate_password(self):
        original = ''
        password = ''

        for i in range(self.pass_len):
            c = random.choice(lower)
            original += c
            password += random.choice(PERMUTATIONS[c])

            print(str(PERMUTATIONS[c]))

        return [original, password]