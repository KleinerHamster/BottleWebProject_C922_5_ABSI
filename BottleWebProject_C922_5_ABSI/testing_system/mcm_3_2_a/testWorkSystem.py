import testing_system.mcm_3_2_a.mcm3and2    # The code to test
import unittest   # The test framework

#Class of testing the conclusion about the operation of the system
class WorkSystemTest(unittest.TestCase):

    #first test
    def test1_conclusionAboutTheWorkSystems(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.conclusionAboutTheWorkSystems("+","+")
                         , "+")

    #second test
    def test2_conclusionAboutTheWorkSystems(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.conclusionAboutTheWorkSystems("+","-")
                         , "-")

    #third test
    def test3_conclusionAboutTheWorkSystems(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.conclusionAboutTheWorkSystems("-","+")
                         , "-")

     #fourth test
    def test4_conclusionAboutTheWorkBlock(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.conclusionAboutTheWorkSystems("-","-")
                         , "-")

if __name__ == '__main__':
    unittest.main()

