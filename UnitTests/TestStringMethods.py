import unittest
from UnitTests import TestFirst

class TestStringMethods(unittest.TestCase):
    
    def setUp(self):
        print("this is setup")
    
    def tearDown(self):
        print("this is tear down")

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    
    def suite(self):
        loader = unittest.TestLoader();
        suite = unittest.TestSuite()
        suite1 = loader.loadTestsFromTestCase("TestFirst")
        print("suite")
        print(type(suite1))
        
        suite.addTest(TestStringMethods('test_upper'))
        suite.addTest(TestStringMethods('test_isupper'))
        suite.addTest(TestFirst.TestFirstClass('test_firstMethod'))

        return suite

    if __name__ == '__main__':
        runner = unittest.TextTestRunner()
        runner.run(suite())
        