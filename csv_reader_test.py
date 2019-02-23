import unittest
from csv_reader import CSVReader

class TestCSVReader(unittest.TestCase):
    def setUp(self):
        pass
    
    def testFileExists(self):
        expectedValue = [['rafiar', 'rahmansyah', 'borneo', 'tangerang', 'pegipegi'], ['nafiar', 'rahmansyah', 'borneo', 'tangerang', 'tokopedia']]
        self.assertEqual(CSVReader("rafiar.csv").readCsv,expectedValue)

    def testFileNotExist(self):
        expectedValue = []
        self.assertEqual(CSVReader("rafiar.csv").readCsv,expectedValue)

if __name__ == "__main__":
    unittest.main()