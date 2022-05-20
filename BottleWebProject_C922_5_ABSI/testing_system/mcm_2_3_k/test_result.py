import unittest
import mcm_2_3_k

class Test_test_result(unittest.TestCase):
        
    def test_itog(self):
        self.assertEqual(mcm_2_3_k.function_itog(0.8,0.9, 0.7,0.75,0.8,80),0.0403)
    def test_itog_2_2(self):
        self.assertEqual(mcm_2_3_k.function_itog(0.28,0.01, 0.01,0.01,1,80),0.0247)
    def test_itog_3(self):
        self.assertEqual(mcm_2_3_k.function_itog(0,0,0,0,0,80),0)
    def test_itog_4(self):
        self.assertEqual(mcm_2_3_k.function_itog(1,1,1,1,1,80),0)
    def test_itog_5(self):
        self.assertEqual(mcm_2_3_k.function_itog(0.38,1, 0.59,0.01,0.29,80),0.0132)
        
if __name__ == '__main__':
    unittest.main()


         







