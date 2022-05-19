import testing_system.mcm_3_2_a.mcm3and2    # The code to test
import unittest   # The test framework

class P2(unittest.TestCase):

    def test1_P2(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.p2(0.7,0.78)
                         , 0.934)

    def test2_P2(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.p2(0.65,0.94)
                         , 0.979)

    def test3_P2(self):
        self.assertEqual(testing_system.mcm_3_2_a.mcm3and2.p2(0.3,0.52)
                         , 0.664)

if __name__ == '__main__':
    unittest.main()



