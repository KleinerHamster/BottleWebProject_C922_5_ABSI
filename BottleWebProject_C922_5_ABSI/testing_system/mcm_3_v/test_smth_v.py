import unittest
import mcm_3

class TestUM(unittest.TestCase):

    # checking the correctness of the calculation of the time of receipt of applications
    def test_application_receipt_1(self):
        self.assertEqual(mcm_3.moment_of_receipt_of_the_application(0.32,32,23), 23.036)

    def test_application_receipt_2(self):
        self.assertEqual(mcm_3.moment_of_receipt_of_the_application(0.24, 0.42, 2494), 2497.398)

    def test_application_receipt_3(self):
        self.assertEqual(mcm_3.moment_of_receipt_of_the_application(0.89, 8429.32, 0.323), 0.323)

    def test_application_receipt_4(self):
        self.assertEqual(mcm_3.moment_of_receipt_of_the_application(0.07, 23, 69), 69.116)

    def test_application_receipt_5(self):
        self.assertEqual(mcm_3.moment_of_receipt_of_the_application(0.01, 100, 1), 1.046)

    # checking the calculation of the end time of channel maintenance by different channels
    def test_filling_channel_1(self):
        self.assertEqual(mcm_3.filling_channel([0.4,'',''],5.662,0.4), [6.062,'',''])

    def test_filling_channel_2(self):
        self.assertEqual(mcm_3.filling_channel([84.137,0,0],83.777,0.4), [84.137,84.177,0])

    def test_filling_channel_3(self):
        self.assertEqual(mcm_3.filling_channel([231.146, 231.197,231.197],242.612,0.42), [243.032, 231.197,231.197])

    def test_filling_channel_4(self):
        self.assertEqual(mcm_3.filling_channel([0,0,0,0],0.01,0.4), [0.41,0,0,0])

    def test_filling_channel_5(self):
        self.assertEqual(mcm_3.filling_channel([89.53,98,24,85],10,98), [89.53,98,24,85])

    # the application has been serviced or refused
    def test_request_counter_1(self):
        self.assertTrue(mcm_3.request_counter([23.39,24.90,25.42]))

    def test_request_counter_2(self):
        self.assertFalse(mcm_3.request_counter(['','','']))

    def test_request_counter_3(self):
        self.assertTrue(mcm_3.request_counter([23.39,'','']))

    def test_request_counter_4(self):
        self.assertTrue(mcm_3.request_counter([89,19.32,'']))

    def test_request_counter_5(self):
        self.assertTrue(mcm_3.request_counter([12.43,15.25,24.24]))

    # checking the calculation of the mathematical expectation (the average value of all tests performed)
    def test_check_result_1(self):
        self.assertEqual(mcm_3.check_result([43,24,54,23]), 36)

    def test_check_result_2(self):
        self.assertEqual(mcm_3.check_result([1,4,4]), 3)

    def test_check_result_3(self):
        self.assertEqual(mcm_3.check_result([43, 24, 54, 23, 56, 244]), 74)

    def test_check_result_4(self):
        self.assertEqual(mcm_3.check_result([3,3,3,3,]), 3)

    def test_check_result_5(self):
        self.assertEqual(mcm_3.check_result([538, 583, 293, 983, 842]), 647.8)


if __name__ == '__main__':
    unittest.main()
