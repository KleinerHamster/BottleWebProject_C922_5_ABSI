import testing_system.mcm_3_2_a.mcm3and2    # The code to test
import unittest   # The test framework

class WorkSystemTest(unittest.TestCase):

    def test1_conclusionAboutTheWorkSystems(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.conclusionAboutTheWorkSystems("+","+")
                         , "+")

    def test2_conclusionAboutTheWorkSystems(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.conclusionAboutTheWorkSystems("+","-")
                         , "-")

    def test3_conclusionAboutTheWorkSystems(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.conclusionAboutTheWorkSystems("-","+")
                         , "-")

    def test4_conclusionAboutTheWorkBlock(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.conclusionAboutTheWorkSystems("-","-")
                         , "-")

if __name__ == '__main__':
    unittest.main()

