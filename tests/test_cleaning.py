from pydoc import text
import unittest
from pysquale.words.cleaning import remove_accentuation, remove_email, remove_extra_spaces, remove_html, remove_numbers, remove_punctuation, to_lower

class TestCleaning(unittest.TestCase):
    def test_remove_accentuation(self):
        text = "É isso aí, irmão! Pensou que seria fácil?"
        real_output = remove_accentuation(text)
        expected_output = "E isso ai, irmao! Pensou que seria facil?"
        self.assertEqual(real_output, expected_output, "Should be equal")

    def test_remove_punctuation(self):
        text = "É isso aí, irmão! Pensou que seria fácil?"
        real_output = remove_punctuation(text)
        expected_output = "É isso aí irmão Pensou que seria fácil"
        self.assertEqual(real_output, expected_output, "Should be equal")

    def test_to_lower(self):
        text = "É isso aí, irmão! Pensou que seria fácil?"
        real_output = to_lower(text)
        expected_output = "é isso aí, irmão! pensou que seria fácil?"
        self.assertEqual(real_output, expected_output, "Should be equal")
    
    def test_remove_numbers(self):
        text = "Um dos 10 números mais fáceis de gravar são o 0800 e o 25696969 Insetisan"
        real_output = remove_numbers(text)
        expected_output = "Um dos   números mais fáceis de gravar são o   e o   Insetisan"
        self.assertEqual(real_output, expected_output, "Should be equal")

    def test_remove_email(self):
        text = "Anota os nossos emails henrique_@mail.com e santana@mail.com , beleza? O @ não deveria ser email.com"
        real_output = remove_email(text)
        expected_output = "Anota os nossos emails  e  , beleza? O  não deveria ser email.com"
        self.assertEqual(real_output, expected_output, "Should be equal")

    def test_remove_html(self):
        text = """<p>Pasquale foi o idealizador do programa da <a href="/wiki/TV_Cultura" title="TV Cultura">TV Cultura</a> <i>Nossa Língua Portuguesa</i> e <a href="/wiki/Colunista" title="Colunista">colunista</a> do jornal <i><a href="/wiki/Folha_de_S.Paulo" title="Folha de S.Paulo">Folha de S.Paulo</a></i> até dezembro de 2016.<sup id="cite_ref-1" class="reference"><a href="#cite_note-1"><span>[</span>1<span>]</span></a></sup> Atualmente, apresenta o programa diário na rádio <a href="/wiki/CBN_S%C3%A3o_Paulo" title="CBN São Paulo">CBN</a> <i>A Nossa Língua de Todo Dia</i>, transmitido às 15h30.<sup id="cite_ref-2" class="reference"><a href="#cite_note-2"><span>[</span>2<span>]</span></a></sup></p>"""
        real_output = remove_html(text)
        expected_output = "Pasquale foi o idealizador do programa da TV Cultura Nossa Língua Portuguesa e colunista do jornal Folha de S.Paulo até dezembro de 2016.[1] Atualmente, apresenta o programa diário na rádio CBN A Nossa Língua de Todo Dia, transmitido às 15h30.[2]"
        self.assertEqual(real_output, expected_output, "Should be equal")
    
    def test_remove_extra_spaces(self):
        text = "    Olha só  quem   vem   lá       .     "
        real_output = remove_extra_spaces(text)
        expected_output = "Olha só quem vem lá."
        self.assertEqual(real_output, expected_output, "Should be equal")

if __name__ == '__main__':
    unittest.main(verbosity=2)
