
# Este Módulo tem as funcionalidade de utulizar o módulo steam_games, importanndo a Classe SteamGames
# e analisar os dados do arquivo "CSV".
# 1. Importar a classe
# 2. Identificar o path do arquivo CSV e fazer a leitura
# 3. Criar o objeto da classe
# Apresenta os resultados

from pathlib import Path

# Importa a classe SteamGames
from steam_games import SteamGames

pasta_programa = Path(__file__).resolve().parent # Identifica a pasta onde está localizado este programa

# Identifica o caminho do arquivo CSV
caminho_csv = pasta_programa / "steam_games.csv" 
# importante manter os arquivos em uma única pasta (Fase_1.py; steam_games.py e steams_games.csv)

# Cria um objeto da classe SteamGames
dados = SteamGames(caminho_csv)

# A amostra de 20 jogos já foi gerada e validada separadamente.
# O método gerar_amostra() permanece disponível na classe SteamGames.

# Apresenta os resultados iniciais
print("ANÁLISE DA BASE DE DADOS | STEAM")
print("-------------****---------------")
print()
#print("Arquivo:", dados.caminho_csv) " foi inserido para verificar se o programa estava localizando corretamente o path"
print("Quantidade de colunas:", len(dados.colunas))
print("Quantidade de jogos:", dados.contar_jogos())

# Executa a análise de jogos gratuitos e pagos
resultado = dados.calcular_perc_free_paid()

#Realiza a análise dos anos com maior número de lançamentos
resultado_ano = dados.calcular_ano_maior_lancamentos()

# Executa a análise de compatibilidade dos sistemas operacionais
resultado_sistemas = dados.calcular_compatibilidade_sistemas()

# Apresenta os resultados
print("\nANÁLISE DE JOGOS GRATUITOS E PAGOS")
print("-------------&&&&-------------------")
print("Quantidade de jogos gratuitos:", resultado["gratuitos"])
print("Quantidade de jogos pagos:", resultado["pagos"])
print("Percentual de jogos gratuitos:",round(resultado["percentual_gratuitos"], 2), "%")
print("Percentual de jogos pagos:",round(resultado["percentual_pagos"], 2), "%")

print("\nANÁLISE DE LANÇAMENTOS POR ANO")
print("--------------------------------")
print("Ano(s) com maior quantidade de lançamentos:", resultado_ano["anos"])
print("Quantidade de jogos lançados:", resultado_ano["quantidade"],"\n")

# Apresenta os resultados da compatibilidades entre Sistemas Op.
print("\nANÁLISE DE COMPATIBILIDADE DOS SISTEMAS OPERACIONAIS")
print("------------------------------------------------------")
print("Total de jogos pagos:", resultado_sistemas["total_pagos"],"\n")

print("\nCOMPATIBILIDADE INDIVIDUAL")
print("----------------------------")
print("Windows:", resultado_sistemas["windows"],"-", round(resultado_sistemas["percentual_windows"], 2), "%")
print("Mac:", resultado_sistemas["mac"],"-", round(resultado_sistemas["percentual_mac"], 2), "%")
print("Linux:", resultado_sistemas["linux"],"-", round(resultado_sistemas["percentual_linux"], 2), "%","\n")

print("\nCOMPATIBILIDADE ENTRE DOIS SISTEMAS")
print("-------------------------------------")
print("Windows e Mac:", resultado_sistemas["windows_mac"],
      "-", round(resultado_sistemas["percentual_windows_mac"], 2), "%")
print("Windows e Linux:", resultado_sistemas["windows_linux"],
      "-", round(resultado_sistemas["percentual_windows_linux"], 2), "%")
print("Linux e Mac:", resultado_sistemas["linux_mac"],"-", round(resultado_sistemas["percentual_linux_mac"], 2), "%","\n")

print("\nCOMPATIBILIDADE ENTRE OS TRÊS SISTEMAS")
print("----------------------------------------")
print("Windows, Mac e Linux:", resultado_sistemas["windows_mac_linux"], "-", round(resultado_sistemas["percentual_windows_mac_linux"], 2), "%","\n")