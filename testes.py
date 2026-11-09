import unittest
import csv
import tempfile

"""
Módulo responsável pela execução dos testes automatizados
da classe SteamGames.Utiliza a biblioteca unittest, disponibilizada na biblioteca
padrão do Python, para verificar se os resultados calculados
pelos métodos desenvolvidos correspondem aos resultados
obtidos manualmente por meio da planilha Excel.
"""
from pathlib import Path

from steam_games import SteamGames

class TesteSteamGames(unittest.TestCase):

    def setUp(self): # Prepara os dados necessários antes de cada teste.
        # permite idemtificar a pasta onde está o arquivo de "testes.py"
        pasta = Path(__file__).resolve().parent
       
        # Define o caminho do arquivo da amostra
        caminho_amostra = pasta / "amostra_steam_games.csv"

        # Cria o objeto utilizando a amostra oficial
        self.dados = SteamGames(caminho_amostra)

    def test_jogos_gratuitos_e_pagos(self):

        # Executa o método desenvolvido na classe
        resultado = self.dados.calcular_perc_free_paid()

        # Apresenta os resultados calculados pelo Python
        print("\nQUESTÃO 1 - JOGOS GRATUITOS E PAGOS")
        print("--------------------------------------")
        print("Quantidade de jogos gratuitos:", resultado["gratuitos"])
        print("Quantidade de jogos pagos:", resultado["pagos"])
        print("Percentual de jogos gratuitos:",
              round(resultado["percentual_gratuitos"], 2), "%")
        print("Percentual de jogos pagos:",
              round(resultado["percentual_pagos"], 2), "%")

        # Compara os resultados com os cálculos manuais do Excel (dados oriundo da base calculada manualmente)
        # Verifica se dois valores são iguais.
        self.assertEqual(resultado["gratuitos"], 2)
        self.assertEqual(resultado["pagos"], 18)

        #Verifica se dois valores numéricos são aproximadamente iguais.
        #Necessário por se tratar de valores em percentuais 
        self.assertAlmostEqual(resultado["percentual_gratuitos"], 10.0)
        self.assertAlmostEqual(resultado["percentual_pagos"], 90.0)

    def test_ano_maior_lancamentos(self):

        # Executa o método desenvolvido na classe
        resultado = self.dados.calcular_ano_maior_lancamentos()

        # Compara os resultados com os cálcuulos manuais da planila  Excel
        self.assertEqual(resultado["anos"], [2023])
        self.assertEqual(resultado["quantidade"], 6)

    
    def test_ano_maior_lancamentos_com_empate(self):

        # Cria um arquivo CSV temporário para simular uma situação de empate
        with tempfile.TemporaryDirectory() as pasta_temporaria:

            # Define o caminho do arquivo temporário
            caminho_teste = Path(pasta_temporaria) / "teste_empate.csv"

            # Cria o arquivo CSV com os lançamentos simulados
            with open(caminho_teste, "w", newline="", encoding="utf-8") as arquivo:

                escritor = csv.writer(arquivo)

                # Insere o cabeçalho
                escritor.writerow(["Release date"])

                # Insere os anos e suas respectivas quantidades
                for ano, quantidade in {
                    2020: 5,
                    2021: 8,
                    2022: 8,
                    2023: 3
                }.items():

                    for i in range(quantidade):
                        escritor.writerow([str(ano)])

            # Instancia a classe utilizando o arquivo temporário
            dados_teste = SteamGames(caminho_teste)

            # Executa o método original da classe
            resultado = dados_teste.calcular_ano_maior_lancamentos()

            # Verifica se todos os anos empatados foram identificados
            self.assertEqual(resultado["anos"], [2021, 2022])

            # Verifica a maior quantidade de lançamentos
            self.assertEqual(resultado["quantidade"], 8)      

   
    def test_compatibilidade_sistemas(self):

        # Executa o método desenvolvido na classe
        resultado = self.dados.calcular_compatibilidade_sistemas()

        # Compara os resultados com os cálculos manuais do Excel
        self.assertEqual(resultado["total_pagos"], 18)

        self.assertEqual(resultado["windows"], 18)
        self.assertEqual(resultado["mac"], 7)
        self.assertEqual(resultado["linux"], 4)

        self.assertEqual(resultado["windows_mac"], 7)
        self.assertEqual(resultado["windows_linux"], 4)
        self.assertEqual(resultado["linux_mac"], 3)
        self.assertEqual(resultado["windows_mac_linux"], 3)

        # Verifica os percentuais
        self.assertAlmostEqual(resultado["percentual_windows"], 100.0)
        self.assertAlmostEqual(resultado["percentual_mac"], 38.89, places=2)
        self.assertAlmostEqual(resultado["percentual_linux"], 22.22, places=2)


if __name__ == "__main__":
    unittest.main()