import unittest
import mcm_2_3_k

class Test_test_Count(unittest.TestCase):
    def test_system_work_count(self):
        self.assertEqual(mcm_2_3_k.system_work_count(0.8,0.9, 0.7,0.75,0.8,80) ,74 )

if __name__ == '__main__':
    unittest.main()


         






