import unittest
import mcm_2_3_k

class Test_test_P(unittest.TestCase):
    def test_A(self):
        self.assertEqual(mcm_2_3_k.function_P(0.8,0.9, 0.7,0.75,0.8,80), 0.925)
    def test_A_2(self):
        self.assertEqual(mcm_2_3_k.function_P(0.28,0.01, 0.01,0.01,1,80), 0.2625)
    def test_A_3(self):
        self.assertEqual(mcm_2_3_k.function_P(0,0,0,0,0,80),0)
    def test_A_4(self):
        self.assertEqual(mcm_2_3_k.function_P(1,1,1,1,1,80), 1)
    def test_A_5(self):
        self.assertEqual(mcm_2_3_k.function_P(0.38,1, 0.59,0.01,0.29,80), 0.725)
if __name__ == '__main__':
    unittest.main()
