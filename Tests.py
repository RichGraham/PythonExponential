import unittest
import exponential
class Initialise(unittest.TestCase):

    def test_at_x_equals_1(self):
        actual = exponential.eval_exp(1.0, n_terms=10)
        expected = 2.7182818284590452353602874713526624977572470936
        self.assertAlmostEqual(actual , expected)


unittest.main(argv=['first-arg-is-ignored'], exit=False)