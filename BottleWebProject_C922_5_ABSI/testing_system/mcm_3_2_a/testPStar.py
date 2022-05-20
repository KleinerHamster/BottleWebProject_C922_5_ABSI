import testing_system.mcm_3_2_a.mcm3and2   # The code to test
import unittest   # The test framework

#Class of testing relative frequency calculation
class PStar(unittest.TestCase):

    #first test
    def test1_PStar(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.pStar(95,100)
                         , 0.95)
        
    #second test
    def test2_PStar(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.pStar(1,5)
                         , 0.2)

    #third test
    def test3_PStar(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.pStar(65,80)
                         , 0.812)

     #fourth test
    def test4_PStar(self):
        self.assertEqual(mcm3and2.pStar(30,40)
                         , 0.75)

    #fifth test
    def test5_PStar(self):
        self.assertEqual(mcm3and2.pStar(5,8)
                         , 0.625)

if __name__ == '__main__':
    unittest.main()



