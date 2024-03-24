import unittest

from block_errors import BlockErrors


class TestBlockErrors(unittest.TestCase):

    def test_div_to_zero(self):
        err_types = {ZeroDivisionError, TypeError}
        try:
            with BlockErrors(err_types):
                a = 1 / 0
        except:
            self.fail()

    def test_div_to_string_zero(self):
        errors = {ZeroDivisionError}
        try:
            with BlockErrors(errors):
                a = 1 / '0'
        except:
            self.fail()

    def test_inner_block(self):
        outer_err_types = {TypeError}
        inner_err_types = {ZeroDivisionError}
        try:
            with BlockErrors(outer_err_types):
                with BlockErrors(inner_err_types):
                    a = 1 / '0'
        except:
            self.fail()

    def test_daughter_error(self):
        err_types = {Exception}
        try:
            with BlockErrors(err_types):
                a = 1 / '0'
        except:
            self.fail()
