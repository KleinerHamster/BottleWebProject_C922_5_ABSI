import unittest
import mcm_2_3_k

class Test_test_P2(unittest.TestCase):
   
    def test_system_P2(self):
        self.assertEqual(mcm_2_3_k.f_P2(0.7,0.75,0.8),0.985)
if __name__ == '__main__':
    unittest.main()


         







