import unittest
import mcm_2_3_k

class Test_test_P1(unittest.TestCase):
    
    def test_system_P1(self):
        self.assertEqual(mcm_2_3_k.f_P1(0.8, 0.9),0.98)
    
  
if __name__ == '__main__':
    unittest.main()


         







