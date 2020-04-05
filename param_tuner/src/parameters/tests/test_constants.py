
import unittest

from param_tuner.src.parameters.constants import InputHanger


class TestInputHanger(unittest.TestCase):
    def test_get_parameters(self):
        hanger = InputHanger()
        another_hanger = InputHanger()
        self.assertEqual(hanger, another_hanger)