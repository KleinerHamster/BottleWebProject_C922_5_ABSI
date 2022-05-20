import unittest
import mcm_4

class TestUM(unittest.TestCase):

    # checking the correctness of the calculation of the time of receipt of applications
    def test_application_receipt_1(self):
        self.assertEqual(mcm_4.moment_of_receipt_of_the_application(0.32,32,23), 23.036)

    def test_application_receipt_2(self):
        self.assertEqual(mcm_4.moment_of_receipt_of_the_application(0.24, 0.42, 2494), 2497.398)

    def test_application_receipt_3(self):
        self.assertEqual(mcm_4.moment_of_receipt_of_the_application(0.89, 8429.32, 0.323), 0.323)

    def test_application_receipt_4(self):
        self.assertEqual(mcm_4.moment_of_receipt_of_the_application(0.07, 23, 69), 69.116)

    def test_application_receipt_5(self):
        self.assertEqual(mcm_4.moment_of_receipt_of_the_application(0.01, 100, 1), 1.046)

    # checking the calculation of the end time of channel maintenance by different channels
    def test_filling_channel_1(self):
        self.assertEqual(mcm_4.filling_channel([23.39,24.90,25.42,86.45],23,42), [23.39,24.90,25.42,86.45])

    def test_filling_channel_2(self):
        self.assertEqual(mcm_4.filling_channel([43,245,53,25],89,38), [127,245,53,25])

    def test_filling_channel_3(self):
        self.assertEqual(mcm_4.filling_channel([0.01,0.01,0.01,0.01],0.01,90), [90.01,0.01,0.01,0.01])

    def test_filling_channel_4(self):
        self.assertEqual(mcm_4.filling_channel([0,0,0,0],0.01,0.4), [0.41,0,0,0])

    def test_filling_channel_5(self):
        self.assertEqual(mcm_4.filling_channel([89.53,98,24,85],10,98), [89.53,98,24,85])

    # the application has been serviced or refused
    def test_request_counter_1(self):
        self.assertTrue(mcm_4.request_counter([23.39,24.90,25.42,86.45]))

    def test_request_counter_2(self):
        self.assertFalse(mcm_4.request_counter(['','','','']))

    def test_request_counter_3(self):
        self.assertTrue(mcm_4.request_counter([23.39,'','','']))

    def test_request_counter_4(self):
        self.assertTrue(mcm_4.request_counter([89,19.32,'','']))

    def test_request_counter_5(self):
        self.assertTrue(mcm_4.request_counter([12.43,15.25,24.24,'']))

    # checking the calculation of the mathematical expectation (the average value of all tests performed)
    def test_check_result_1(self):
        self.assertEqual(mcm_4.check_result([43,24,54,23]), 36)

    def test_check_result_2(self):
        self.assertEqual(mcm_4.check_result([1,4,4]), 3)

    def test_check_result_3(self):
        self.assertEqual(mcm_4.check_result([43, 24, 54, 23, 56, 244]), 74)

    def test_check_result_4(self):
        self.assertEqual(mcm_4.check_result([3,3,3,3,]), 3)

    def test_check_result_5(self):
        self.assertEqual(mcm_4.check_result([538, 583, 293, 983, 842]), 647.8)


if __name__ == '__main__':
    unittest.main()
