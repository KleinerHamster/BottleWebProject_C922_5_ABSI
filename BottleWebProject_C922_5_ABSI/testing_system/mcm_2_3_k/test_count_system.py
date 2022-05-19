import unittest
import mcm_2_3_k

class Test_test_P(unittest.TestCase):
    def test_A(self):
        self.assertEqual(mcm_2_3_k.function_P(0.8,0.9, 0.7,0.75,0.8,80), 0.925)
    
    def test_system_work_count(self):
        self.assertEqual(mcm_2_3_k.system_work_count(0.8,0.9, 0.7,0.75,0.8,80) ,74 )
    
    def test_system_P1(self):
        self.assertEqual(mcm_2_3_k.f_P1(0.8, 0.9),0.98)
    
    def test_system_P2(self):
        self.assertEqual(mcm_2_3_k.f_P2(0.7,0.75,0.8),0.985)
        
    def test_itog(self):
        self.assertEqual(mcm_2_3_k.function_itog(0.8,0.9, 0.7,0.75,0.8,80),0.0403)

if __name__ == '__main__':
    unittest.main()


         






