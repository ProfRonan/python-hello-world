"""Esse arquivo testa o arquivo main.py"""

import importlib  # para importar o módulo main dinamicamente
import io  # para capturar a saída do print
import sys  # para restaurar o stdout padrão e remover o módulo main do cache
import unittest  # para criar o caso de teste
from unittest.mock import patch  # para simular a entrada do usuário


class TestMain(unittest.TestCase):
    """Classe que testa o arquivo main.py"""

    def setUp(self):
        """
        Inicializa o ambiente de teste removendo o módulo principal do cache.
        Isso é necessário para ser capaz de importá-lo novamente em cada teste.
        """
        sys.modules.pop("main", None)

    @patch("builtins.input", return_value="Alice")
    def test_prints_hello_Alice(self, _mock_input):
        """
        Testa se o arquivo main.py imprime a saída correta
        quando o usuário é Alice
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertEqual("oi, Alice!", captured_output.getvalue().strip())

    @patch("builtins.input", return_value="Bernardo")
    def test_prints_hello_other_Bernardo(self, _mock_input):
        """
        Testa se o arquivo main.py imprime a saída correta quando o usuário é Bernardo
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertEqual("oi, Bernardo!", captured_output.getvalue().strip())
