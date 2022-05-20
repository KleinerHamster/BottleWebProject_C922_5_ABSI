import testing_system.mcm_3_2_a.mcm3and2 # The code to test
import unittest   # The test framework

#Class of testing calculation of system reliability
class P(unittest.TestCase):

    #first test
    def test1_P(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.p(0.997,0.934)
                         , 0.931)

    #second test
    def test2_P(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.p(0.894,0.997)
                         , 0.891)

    #third test
    def test3_P(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.p(0.694,0.896)
                         , 0.622)

    #fourth test
    def test4_P(self):
        self.assertEqual(mcm3and2.p(0.356,0.764)
                         , 0.272)

    #fifth test
    def test5_P(self):
        self.assertEqual(mcm3and2.p(0.859,0.997)
                         , 0.856)

if __name__ == '__main__':
    unittest.main()


