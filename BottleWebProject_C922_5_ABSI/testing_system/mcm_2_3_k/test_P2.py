import unittest
import mcm_2_3_k

class Test_test_P2(unittest.TestCase):
   
    def test_system_P2(self):
        self.assertEqual(mcm_2_3_k.f_P2(0.7,0.75,0.8),0.985)
    def test_system_P2_2(self):
        self.assertEqual(mcm_2_3_k.f_P2(0.01,0.01,1),1)
    def test_system_P2_3(self):
        self.assertEqual(mcm_2_3_k.f_P2(0,0,0),0)
    def test_system_P2_4(self):
        self.assertEqual(mcm_2_3_k.f_P2(1,1,1),1)
    def test_system_P2_5(self):
        self.assertEqual(mcm_2_3_k.f_P2(0.59,0.01,0.29),0.711811)

      

if __name__ == '__main__':
    unittest.main()

         







