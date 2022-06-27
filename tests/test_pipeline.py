import unittest
from pysquale.common.pipeline import MapperPipeline, ReducerPipeline
from pysquale.words.cleaning import remove_accentuation, remove_punctuation, to_lower

class TestPipeline(unittest.TestCase):
    def test_reducer_pipeline(self):
        func_list = [to_lower, remove_accentuation, remove_punctuation]
        text = "Olá, quem é você?"
        pipe = ReducerPipeline(target=text, items=func_list)
        real_output = pipe.run()
        expected_output = "ola quem e voce"
        self.assertEqual(real_output, expected_output, "Should be equal")

    def test_mapper_pipeline(self):
        func = remove_accentuation
        text_list = ["Hortência", "Sebastião", "José"]
        pipe = MapperPipeline(target=func, items=text_list)
        real_output = pipe.run()
        expected_output = ["Hortencia", "Sebastiao", "Jose"]
        self.assertEqual(real_output, expected_output, "Should be equal")

if __name__ == '__main__':
    unittest.main(verbosity=2)