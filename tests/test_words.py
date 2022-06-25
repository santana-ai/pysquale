import unittest
from src.words import ABBREVIATION_MAP

class TestWords(unittest.TestCase):
    def test_abbreviation_map(self):
        text = 'tlgd'
        abbreviation_dict = ABBREVIATION_MAP
        real_output = abbreviation_dict.get(text)
        expected_output = "está ligado"
        self.assertEqual(real_output, expected_output, "Should be equal")

if __name__ == '__main__':
    unittest.main(verbosity=2)
