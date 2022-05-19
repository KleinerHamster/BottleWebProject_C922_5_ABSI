import unittest
import testing_system.mcm_3_2_a.mcm3and2    # The code to test
#import unittest   # The test framework

class WorkBlocksTest(unittest.TestCase):

    def test1_conclusionAboutTheWorkBlock(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.conclusionAboutTheWorkBlock("+","+","-","-","+")
                         , ["+","+"])

    def test2_conclusionAboutTheWorkBlock(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.conclusionAboutTheWorkBlock("+","+","+","-","-")
                         , ["+","-"])

    def test3_conclusionAboutTheWorkBlock(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.conclusionAboutTheWorkBlock("-","-","-","+","+")
                         , ["-","+"])

    def test4_conclusionAboutTheWorkBlock(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.conclusionAboutTheWorkBlock("-","-","-","-","-")
                         , ["-","-"])

if __name__ == '__main__':
    unittest.main()

