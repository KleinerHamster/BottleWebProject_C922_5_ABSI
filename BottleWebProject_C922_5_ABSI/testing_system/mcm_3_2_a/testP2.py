import testing_system.mcm_3_2_a.mcm3and2    # The code to test
import unittest   # The test framework

#Class of testing calculation of the probability of failure-free operation of the second block
class P2(unittest.TestCase):

    #first test
    def test1_P2(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.p2(0.7,0.78)
                         , 0.934)

    #second test
    def test2_P2(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.p2(0.65,0.94)
                         , 0.979)

    #third test
    def test3_P2(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.p2(0.3,0.52)
                         , 0.664)

     #fourth test
    def test4_P2(self):
        self.assertEqual(mcm3and2.p2(0.89,0.11)
                            , 0.902)

    #fifth test
    def test5_P2(self):
        self.assertEqual(mcm3and2.p2(0.23,0.77)
                         , 0.823)

if __name__ == '__main__':
    unittest.main()



