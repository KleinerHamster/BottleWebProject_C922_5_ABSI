import testing_system.mcm_3_2_a.mcm3and2   # The code to test
import unittest   # The test framework

class PPStar(unittest.TestCase):

    def test1_PPStar(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.p_pStar(0.95,0.931)
                         , 0.019)

    def test2_PPStar(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.p_pStar(0.78,0.876)
                         , 0.096)

    def test3_PPStar(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.p_pStar(0.69,0.699)
                         , 0.009)

    def test4_PPStar(self):
        self.assertEqual(mcm3and2.p_pStar(0.25,0.782)
                         , 0.532)

    def test5_PPStar(self):
        self.assertEqual(mcm3and2.p_pStar(0.51,0.551)
                         , 0.041)

if __name__ == '__main__':
    unittest.main()


