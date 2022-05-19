import unittest
import mcm_2_3_k

class Test_test_P(unittest.TestCase):
    def test_A(self):
        self.assertEqual(mcm_2_3_k.function_P(0.8,0.9, 0.7,0.75,0.8,80), 0.925)
   

if __name__ == '__main__':
    unittest.main()


         







