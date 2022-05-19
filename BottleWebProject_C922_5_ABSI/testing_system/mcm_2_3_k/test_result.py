import unittest
import mcm_2_3_k

class Test_test_result(unittest.TestCase):
        
    def test_itog(self):
        self.assertEqual(mcm_2_3_k.function_itog(0.8,0.9, 0.7,0.75,0.8,80),0.0403)

if __name__ == '__main__':
    unittest.main()


         







