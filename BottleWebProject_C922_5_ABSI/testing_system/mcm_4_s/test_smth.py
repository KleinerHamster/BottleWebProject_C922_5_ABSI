import unittest
import mcm_4

class TestUM(unittest.TestCase):

    def test_A(self):
        self.assertEqual(mcm_4.moment_of_receipt_of_the_application(0.32,32,23), 23.036)

    def test_B(self):
        self.assertEqual(mcm_4.moment_of_receipt_of_the_application(0.24, 0.42, 2494), 2497.398)

    def test_C(self):
        self.assertEqual(mcm_4.moment_of_receipt_of_the_application(3289, 8429.32, -0.323), -0.324)


    # следующий тест
    def test_a2(self):
        self.assertEqual(mcm_4.link1([23.39,24.90,25.42,86.45],23,42), [23.39,24.90,25.42,86.45])

    def test_b2(self):
        self.assertEqual(mcm_4.link1([43,245,53,25],89,38), [127,245,53,25])


    # следующий тест
    def test_a3(self):
        self.assertEqual(mcm_4.count_of_link([23.39,24.90,25.42,86.45]), True)

    def test_b3(self):
        self.assertEqual(mcm_4.count_of_link(['','','','']), False)


    # next test
    def test_a4(self):
        self.assertEqual(mcm_4.check_result([43,24,54,23]), 36)

    def test_b4(self):
        self.assertEqual(mcm_4.check_result([1,4,4]), 3)


if __name__ == '__main__':
    unittest.main()




