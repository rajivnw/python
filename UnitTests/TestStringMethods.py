import unittest
import Utilitys.HTMLTestRunner as HTMLRunner

class TestStringMethods(unittest.TestCase):
    
    def setUp(self):
        print("this is setup")
        print(self._testMethodName)

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
    
def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestStringMethods('test_upper'))
    suite.addTest(TestStringMethods('test_isupper'))
    return suite

if __name__ == '__main__':
    #runner = unittest.TextTestRunner()
    outfile = open("/Users/rajiv/Documents/Automation/PythonPractice/Report.html", "w")
    
    runner = HTMLRunner.HTMLTestRunner(stream=outfile,title='Test Report',description='This demonstrates the report output by Prasanna.Yelsangikar.')
    
    runner.run(suite())
        