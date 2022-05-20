import unittest
import mcm_2_3_k

class Test_test_Count(unittest.TestCase):
    def test_system_work_count(self):
        self.assertEqual(mcm_2_3_k.system_work_count(0.8,0.9, 0.7,0.75,0.8,80) ,74 )
    def test_system_work_count_1(self):
        self.assertEqual(mcm_2_3_k.system_work_count(0,0, 0,0,0,80) ,0 )
    def test_system_work_count_2(self):
        self.assertEqual(mcm_2_3_k.system_work_count(1,1, 1,1,1,80) ,80 )
    def test_system_work_count_3(self):
        self.assertEqual(mcm_2_3_k.system_work_count(0.28,0.01, 0.01,0.01,1,80) ,21 )
    def test_system_work_count_4(self):
        self.assertEqual(mcm_2_3_k.system_work_count(0.38, 1, 0.59, 0.01,0.29, 80) ,58 )
if __name__ == '__main__':
    unittest.main()

