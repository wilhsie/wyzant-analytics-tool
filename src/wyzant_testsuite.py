from wyzant_object import WyzantWebTester
import unittest


class TestsCrunchyroll(unittest.TestCase):
    def test_tutor_data(self):
        tester = WyzantWebTester()
        tester.grab_tutoring_data()


if __name__ == '__main__':
    unittest.main()
