import unittest
import taxi

class TaxiTest(unittest.TestCase):

    def setUp(self):
        print 'In setUp()'
        self.t1 = taxi.Taxi(100, 'normal')
        self.t2 = taxi.Taxi(100, 'special')
        self.t3 = taxi.Taxi(100, 'somthingelse')


    def tearDown(self):
        print 'In tearDown()'
        del self.t1
        del self.t2
        del self.t3

    def testNormal(self):
        self.failUnlessEqual(self.t1.compute(), 144.0)    

    def testSpecial(self):
        self.failUnlessEqual(self.t2.compute(), 120)    

    def testSomethingElse(self):
        self.failUnlessEqual(self.t3.compute(), None)    

if __name__ == '__main__':
    unittest.main()
    
