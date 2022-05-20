import testing_system.mcm_3_2_a.mcm3and2    # The code to test
import unittest   # The test framework

#Class of testing concluding on the operation of all elements
class WorkElementsTest(unittest.TestCase):

    #first test
    def test1_conclusionAboutTheWorkElement(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.conclusionAboutTheWorkElement(0.8,0.9,0.85,0.7,0.78,
                                                                0.97,0.12,0.48,0.22,0.64)
                         , ["-","+","+","+","+"])

    #second test
    def test2_conclusionAboutTheWorkElement(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.conclusionAboutTheWorkElement(0.9,0.35,0.7,0.85,0.68,
                                                                0.31,0.81,0.88,0.81,0.88)
                         , ["+","-","-","+","-"])

    #third test
    def test3_conclusionAboutTheWorkElement(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.conclusionAboutTheWorkElement(0.75,0.34,0.52,0.29,0.6,
                                                                0.89,0.2,0.48,0.22,0.64)
                         , ["-","+","+","+","-"])

     #fourth test
    def test4_conclusionAboutTheWorkElement(self):
        self.assertEqual(mcm3and2.conclusionAboutTheWorkElement(0.56,0.47,0.31,0.11,0.6,
                                                                0.61,0.5,0.76,0.2,0.65)
                         , ["-","-","-","-","-"])

    #fifth test
    def test5_conclusionAboutTheWorkElement(self):
        self.assertEqual(mcm3and2.conclusionAboutTheWorkElement(0.75,0.34,0.42,0.59,0.97,
                                                                0.7,0.12,0.4,0.12,0.95)
                         , ["+","+","+","+","+"])

if __name__ == '__main__':
    unittest.main()


