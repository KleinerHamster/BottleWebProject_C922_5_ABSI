import unittest
import testing_system.mcm_3_2_a.mcm3and2    # The code to test
#import unittest   # The test framework

#Class of testing concluding the operation of all blocks
class WorkBlocksTest(unittest.TestCase):

    #first test
    def test1_conclusionAboutTheWorkBlock(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.conclusionAboutTheWorkBlock("+","+","-","-","+")
                         , ["+","+"])

    #second test
    def test2_conclusionAboutTheWorkBlock(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.conclusionAboutTheWorkBlock("+","+","+","-","-")
                         , ["+","-"])

    #third test
    def test3_conclusionAboutTheWorkBlock(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.conclusionAboutTheWorkBlock("-","-","-","+","+")
                         , ["-","+"])

     #fourth test
    def test4_conclusionAboutTheWorkBlock(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.conclusionAboutTheWorkBlock("-","-","-","-","-")
                         , ["-","-"])

if __name__ == '__main__':
    unittest.main()

