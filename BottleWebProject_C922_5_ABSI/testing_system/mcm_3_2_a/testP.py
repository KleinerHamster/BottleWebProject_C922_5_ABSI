import testing_system.mcm_3_2_a.mcm3and2    # The code to test
import unittest   # The test framework

class P(unittest.TestCase):

    def test1_P(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.p(0.997,0.934)
                         , 0.931)

    def test2_P(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.p(0.894,0.997)
                         , 0.891)

    def test3_P(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.p(0.694,0.896)
                         , 0.622)

    def test4_P(self):
        self.assertEqual(mcm3and2.p(0.356,0.764)
                         , 0.272)

    def test5_P(self):
        self.assertEqual(mcm3and2.p(0.859,0.997)
                         , 0.856)

if __name__ == '__main__':
    unittest.main()


