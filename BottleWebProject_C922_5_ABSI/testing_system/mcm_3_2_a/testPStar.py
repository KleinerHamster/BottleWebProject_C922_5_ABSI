import testing_system.mcm_3_2_a.mcm3and2   # The code to test
import unittest   # The test framework

class PStar(unittest.TestCase):

    def test1_PStar(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.pStar(95,100)
                         , 0.95)

    def test2_PStar(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.pStar(1,5)
                         , 0.2)

    def test3_PStar(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.pStar(65,80)
                         , 0.812)

if __name__ == '__main__':
    unittest.main()



