import unittest
from pysquale.words.preprocessing import remove_stopwords, tokenize, detokenize, stem

class TestPreprocessing(unittest.TestCase):
    def test_tokenize(self):
        text = "Oiiii galerinha. Os professores da minha escola gostam de jogar bola com os alunos."
        real_output = tokenize(text)
        expected_output = ['oiiii', 'galerinha', '.', 'os',  'professores', 'da', 'minha', 'escola', 'gostam', 'de', 'jogar', 'bola', 'com', 'os', 'alunos', '.']
        self.assertEqual(real_output, expected_output, "Should be equal")

    def test_detokenize(self):
        tokens = ['cidade', 'de', 'deus']
        real_output = detokenize(tokens)
        expected_output = "cidade de deus"
        self.assertEqual(real_output, expected_output, "Should be equal")

    def test_remove_stopwords(self):
        text = "Oiiii galerinha. Os professores da minha escola gostam de jogar bola com os alunos."
        tokens = tokenize(text)
        additinonal_words = ["oiiii"]
        real_output = remove_stopwords(tokens, additinonal_words)
        expected_output = ["galerinha", ".", "professores", "escola", "gostam", "jogar", "bola", "alunos", "."]
        self.assertEqual(real_output, expected_output, "Should be equal")

    def test_stemming(self):
        text = "Joga bola, joga bola Jogador Joga bola, joga bola Corocondô"
        tokens = tokenize(text)
        real_output = stem(tokens)
        expected_output = ["jog", "bol", ",", "jog", "bol", "jog", "jog", "bol",",", "jog", "bol", "corocondô"]
        self.assertEqual(real_output, expected_output, "Should be equal")

if __name__ == '__main__':
    unittest.main(verbosity=2)