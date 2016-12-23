import unittest, csv
from main import load_letters, eng2ara


class Test(unittest.TestCase):

    letters = {}
    tests = {}

    def setUp(self):
        self.letters = load_letters()
        with open("tests.csv", mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            self.tests = {row[0]: row[1] for row in reader}

    def test_table(self):
        for eng, ara in self.tests.items():
            self.assertEqual(ara, eng2ara(eng, self.letters))


if __name__ == '__main__':
    unittest.main()