from unittest import TestCase
from com.jaine.operacoes import Operacoes

class TestOperacoes(TestCase):

    def setUp(self):
        self.operacoes = Operacoes()
    
    def test_soma(self):
        self.assertEqual(self.operacoes.soma([2, 2]), 4, "Deveria ser 4")
