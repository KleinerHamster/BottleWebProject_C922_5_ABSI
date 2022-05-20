import testing_system.mcm_3_2_a.mcm3and2     # The code to test
import unittest   # The test framework

class P1(unittest.TestCase):

    def test1_P1(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.p1(0.8,0.9,0.85)
                         , 0.997)

    def test2_P1(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.p1(0.75,0.5,0.95)
                         , 0.994)

    def test3_P1(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.p1(0.55,0.6,0.3)
                         , 0.874)

    def test4_P1(self):
        self.assertEqual(mcm3and2.p1(0.34,0.89,0.78)
                         , 0.984)

    def test5_P1(self):
        self.assertEqual(mcm3and2.p1(0.96,0.64,0.72)
                         , 0.996)

if __name__ == '__main__':
    unittest.main()


