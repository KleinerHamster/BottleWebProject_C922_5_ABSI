import unittest
import mcm_2_3_k

class Test_test_P1(unittest.TestCase):
    
    def test_system_P1(self):
        self.assertEqual(mcm_2_3_k.f_P1(0.8, 0.9),0.98)
    def test_system_P1_2(self):
        self.assertEqual(mcm_2_3_k.f_P1(0.28,0.01),0.2872)
    def test_system_P1_3(self):
        self.assertEqual(mcm_2_3_k.f_P1(0,0),0)
    def test_system_P1_4(self):
        self.assertEqual(mcm_2_3_k.f_P1(1,1),1)
    def test_system_P1_5(self):
        self.assertEqual(mcm_2_3_k.f_P1(0.38,1),1)
        
if __name__ == '__main__':
    unittest.main()



         







