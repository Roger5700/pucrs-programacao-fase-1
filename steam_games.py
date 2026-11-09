import csv # Permitirá a leitura dos dados oriundos do arquivos com extensão "csv".
import math
import random

from pathlib import Path

class SteamGames:
    """
    Classe responsável por acessar os dados dos jogos da Steam. 
    O caminho do arquivo CSV deve ser informado pelo programa
    que utilizar esta classe. Foi dados o mesmo nome da base dee dados!

    """
   
    def __init__(self, caminho_csv):
        """
        Inicializa a classe SteamGames, armazena o caminho
        do arquivo CSV e verifica se o arquivo possui cabeçalho.
        """

        # Armazena o caminho recebido pelo construtor __init__
        self.caminho_csv = Path(caminho_csv)

        # Verifica se o arquivo existe
        if not self.caminho_csv.is_file():
            raise FileNotFoundError(f"Arquivo não encontrado: {self.caminho_csv}")

        # Abre o arquivo CSV
        arquivo = open(self.caminho_csv, "r", encoding="utf-8")

        try:
            # Realiza a leitura do arquivo
            leitor = csv.reader(arquivo)

            # Lê a primeira linha, que contém o cabeçalho
            cabecalho = next(leitor, None)

        finally:
            # Garante o fechamento do arquivo mitigando travamento
            arquivo.close()

        # Verifica se o arquivo possui cabeçalho
        if cabecalho is None or len(cabecalho) == 0:
            raise ValueError("O arquivo CSV está vazio ou sem cabeçalho.")

        # Armazena os nomes das colunas
        self.colunas = cabecalho

    
    def percorrer_jogos(self):
        """
        Percorre os registros do arquivo CSV e apresenta
        os dados de cada jogo.
        """

        # Abre o arquivo cSV
        arquivo = open(self.caminho_csv, "r", encoding="utf-8")

        try:
            # Realiza a leitura do arquivo
            leitor = csv.reader(arquivo)

            # Pula a primeira linha, que contém o cabeçalho
            next(leitor, None)

            # Percorre os registros do arquivo
            for jogo in leitor:
                print(jogo)

        finally:
            # Garante o fechamento do arquivo
            arquivo.close()

      
    def contar_jogos(self):
        """
        Retorna a quantidade de jogos existentes no arquivo CSV:
        """

        # Inicializa o contador
        contador = 0

        # Abre o arquivo CSV
        arquivo = open(self.caminho_csv, "r", encoding="utf-8")

        try:
            # Realiza a leitura do arquivo
            leitor = csv.reader(arquivo)

            # Pula a primeira linha, que contém o cabeçalho
            next(leitor, None)

            # Percorre os registros do arquivo
            for jogo in leitor:
                contador += 1

        finally:
            # Garante o fechamento do arquivo
            arquivo.close()

        # Retorna a quantidade total de jogos
        return contador


    # método para calcular percentual de jogos gratuitos e pagos
    def calcular_perc_free_paid(self):
        """
        Calcula a quantidade e o percentual de jogos gratuitos e pagos.
        Trata possíveis erros na leitura dos preços e garante o fechamento
        do arquivo CSVv.
        """
        # Inicializa os contadores
        gratuitos = 0
        pagos = 0

        # Verifica se a coluna Price existe no arquivo
        if "Price" not in self.colunas:
            raise ValueError("A coluna Price não foi encontrada no arquivo CSV disponível.")

        # Identifica a posição da coluna Price
        indice_preco = self.colunas.index("Price")

        # Abre o arquivo CSV
        arquivo = open(self.caminho_csv, "r", encoding="utf-8")

        try:
            # Realiza a leitura do arquivo
            leitor = csv.reader(arquivo)

            # Pula a primeira linha, que contém o cabeçalho partindo da premissa que há um cabeçalho
            next(leitor, None)

            # Percorre os registros do arquivo
            for numero_linha, jogo in enumerate(leitor, start=2):

                try:
                    # Converte o preço para número 
                    preco = float(jogo[indice_preco])

                    # Verifica se o preço é um número válido e finito
                    if not math.isfinite(preco):
                        raise ValueError(f"Preço inválido na linha {numero_linha} do arquivo CSV.")

                except (ValueError, IndexError):
                    raise ValueError(f"Preço inválido na linha {numero_linha} do arquivo CSV.")

                # Verifica se o jogo é gratuito ou pago
                if preco == 0:
                    gratuitos += 1
                elif preco > 0:
                    pagos += 1
                else:
                    raise ValueError(f"Preço negativo encontrado na linha {numero_linha}." )

        finally:
            # Garante o fechamento do arquivo, mesmo em caso de erro. mitigando a possibilidade de travamento
            arquivo.close()

        # Calcula a quantidade total de jogos
        total = gratuitos + pagos

        # Calcula os percentuais, evitando divisão por zero
        if total > 0:
            percentual_gratuitos = (gratuitos / total) * 100
            percentual_pagos = (pagos / total) * 100
        else:
            percentual_gratuitos = 0
            percentual_pagos = 0

        # Retorna os resultados em um dicionário
        return {
            "gratuitos": gratuitos,
            "pagos": pagos,
            "percentual_gratuitos": percentual_gratuitos,
            "percentual_pagos": percentual_pagos }


    # Assegurar que será feita a leitura do ano independente da formatação da data inserida
    def identificar_ano(self, data_lancamento):
        """
        Identifica o ano da data de lançamento.
        """
        # Separa as datas e retira as vírgulas e evita erro por valor não string
        partes_data = str(data_lancamento).replace(",", "").split() 

        # Percorre a data
        for parte in partes_data:

            # Verifica se o ano possui quatro caracteres numéricos
            if len(parte) == 4 and parte.isdigit():

                # Retorna o ano identificado
                return int(parte)

        # Retorna None caso não encontre um ano válido
        return None
    
       
    def calcular_ano_maior_lancamentos(self):
        """
        Identifica o ano com maior quantidade de jogos lançados.
        Retorna todos os anos em caso de empate.
        """

        # Inicializa o dicionário para armazenar os anos e as quantidades
        quantidade_por_ano = {}

        # Verifica se a coluna Release date existe
        if "Release date" not in self.colunas:
            raise ValueError("A coluna Release date não foi encontrada no CSV.")

        # Identifica a posição da coluna de data
        indice_data = self.colunas.index("Release date")

        # Abre o arquivo CSV
        arquivo = open(self.caminho_csv, "r", encoding="utf-8")

        try:
            # Realiza a leitura do arquivo
            leitor = csv.reader(arquivo)

            # Pula a primeira linha, que contém o cabeçalho
            next(leitor, None)

            # Percorre os registros do arquivo
            for jogo in leitor:

                # Verifica se o registro possui a coluna de data
                if len(jogo) <= indice_data:
                    continue

                # Identifica a data de lançamento
                data_lancamento = jogo[indice_data].strip()

                # Identifica o ano utilizando o método auxiliar
                ano = self.identificar_ano(data_lancamento)

                # Ignora registros sem ano identificado
                if ano is None:
                    continue

                # Verifica se o ano já existe no dicionário
                if ano in quantidade_por_ano:
                    quantidade_por_ano[ano] += 1
                else:
                    quantidade_por_ano[ano] = 1

        finally:
            # Garante o fechamento do arquivo
            arquivo.close()

        # Verifica se existem anos identificados
        if len(quantidade_por_ano) == 0:
            return {"anos": [], "quantidade": 0}

        # Identifica a maior quantidade de lançamentos
        maior_quantidade = max(quantidade_por_ano.values())

        # Inicializa a lista dos anos com maior quantidade
        anos_maior_lancamento = []

        # Identifica todos os anos que possuem a maior quantidade
        for ano, quantidade in quantidade_por_ano.items():
            if quantidade == maior_quantidade:
                anos_maior_lancamento.append(ano)

        # Coloca os anos em ordem crescente
        anos_maior_lancamento.sort()

        # Retorna os resultados em um dicionário
        return {"anos": anos_maior_lancamento, "quantidade": maior_quantidade }
       
    def calcular_compatibilidade_sistemas(self):
        """
        Calcula a quantidade e o percentual de jogos pagos
        compatíveis com Windows, Mac e Linux, individualmente,
        em combinações de dois sistemas e nos três simultaneamente.
        """

        # Inicializa os contadores
        total_pagos = 0

        windows = 0
        mac = 0
        linux = 0

        windows_mac = 0
        windows_linux = 0
        linux_mac = 0
        windows_mac_linux = 0

        # Verifica se todas as colunas necessárias existem
        colunas_obrigatorias = ["Price", "Windows", "Mac", "Linux"]

        for coluna in colunas_obrigatorias:
            if coluna not in self.colunas:
                raise ValueError(f"A coluna {coluna} não foi encontrada no CSV.")

        # Identifica a posição de cada coluna
        indice_preco = self.colunas.index("Price")
        indice_windows = self.colunas.index("Windows")
        indice_mac = self.colunas.index("Mac")
        indice_linux = self.colunas.index("Linux")

        # Abre o arquivo CSV
        arquivo = open(self.caminho_csv, "r", encoding="utf-8")

        try:
            # Realiza a leitura do arquivo
            leitor = csv.reader(arquivo)

            # Pula a primeira linha, que contém o cabeçalho
            next(leitor, None)

            # Percorre todos os registros do arquivo
            for numero_linha, jogo in enumerate(leitor, start=2):
                try:
                    # Identifica o preço do jogo
                    preco = float(jogo[indice_preco])

                    # Verifica se o preço é um número válido e finito
                    if not math.isfinite(preco):
                        raise ValueError("Preço não finito.")

                except (ValueError, IndexError) as erro:
                    raise ValueError(f"Preço inválido na linha {numero_linha} do CSV.") from erro             
                               
                 # Verifica se o registro possui todas as colunas necessárias
                if len(jogo) <= max(indice_preco, indice_windows, indice_mac, indice_linux):
                    raise ValueError(f"Registro incompleto na linha {numero_linha} do CSV." )

                 # Verifica se o preço é negativo
                if preco < 0:
                    raise ValueError(f"Preço negativo na linha {numero_linha} do CSV." )

               
                # Considera somente os jogos pagos
                if preco > 0:

                    # Verifica os valores de compatibilidade
                    comp_windows = jogo[indice_windows].strip().lower()
                    comp_mac = jogo[indice_mac].strip().lower()
                    comp_linux = jogo[indice_linux].strip().lower()

                    # Valida os valores das três colunas
                    if comp_windows not in ("true", "false") or \
                       comp_mac not in ("true", "false") or \
                       comp_linux not in ("true", "false"):
                        raise ValueError(f"Compatibilidade inválida na linha {numero_linha} do CSV." )

                    # Converte os valores para verdadeiro ou falso
                    comp_windows = comp_windows == "true"
                    comp_mac = comp_mac == "true"
                    comp_linux = comp_linux == "true"

                    total_pagos += 1

                    # Verifica a compatibilidade individual
                    if comp_windows:
                        windows += 1

                    if comp_mac:
                        mac += 1

                    if comp_linux:
                        linux += 1

                    # Verifica a compatibilidade entre dois sistemas
                    if comp_windows and comp_mac:
                        windows_mac += 1

                    if comp_windows and comp_linux:
                        windows_linux += 1

                    if comp_linux and comp_mac:
                        linux_mac += 1

                    # Verifica a compatibilidade simultânea com os três sistemas
                    if comp_windows and comp_mac and comp_linux:
                        windows_mac_linux += 1

        finally:
            # Garante o fechamento do arquivo mesmo em caso de erro
            arquivo.close()

        # Calcula os percentuais sobre o total de jogos pagos
        if total_pagos > 0:

            percentual_windows = (windows / total_pagos) * 100
            percentual_mac = (mac / total_pagos) * 100
            percentual_linux = (linux / total_pagos) * 100

            percentual_windows_mac = (windows_mac / total_pagos) * 100
            percentual_windows_linux = (windows_linux / total_pagos) * 100
            percentual_linux_mac = (linux_mac / total_pagos) * 100

            percentual_windows_mac_linux = (windows_mac_linux / total_pagos) * 100

        else:
            percentual_windows = 0
            percentual_mac = 0
            percentual_linux = 0

            percentual_windows_mac = 0
            percentual_windows_linux = 0
            percentual_linux_mac = 0

            percentual_windows_mac_linux = 0

        # Retorna os resultados da análise
        return {
            "total_pagos": total_pagos,
            "windows": windows,
            "mac": mac,
            "linux": linux,
            "windows_mac": windows_mac,
            "windows_linux": windows_linux,
            "linux_mac": linux_mac,
            "windows_mac_linux": windows_mac_linux,
            "percentual_windows": percentual_windows,
            "percentual_mac": percentual_mac,
            "percentual_linux": percentual_linux,
            "percentual_windows_mac": percentual_windows_mac,
            "percentual_windows_linux": percentual_windows_linux,
            "percentual_linux_mac": percentual_linux_mac,
            "percentual_windows_mac_linux": percentual_windows_mac_linux}

    ##################### Etapa da análise sobre amostra 20 jodos ########################################

    def gerar_amostra(self, quantidade=20):
        
        """
        Gera uma amostra aleatória de jogos, desconsiderando
        os primeiros 20 registros do arquivo original.
        Salva a amostra em um novo arquivo CSV.
        """

        # Abre o arquivo CSV original
        arquivo = open(self.caminho_csv, "r", encoding="utf-8")

        try:
            # Realiza a leitura do arquivo csv
            leitor = csv.reader(arquivo)

            # Armazena o cabeçalho
            cabecalho = next(leitor, None)

            # Armazena os registros dos jogos
            jogos = list(leitor)

        finally:
            # Garante o fechamento do arquivo
            arquivo.close()

        # Desconsidera os primeiros 20 registros
        jogos_disponiveis = jogos[20:]

        # Verifica se existem registros suficientes pois poderá haver uma amostra inferior a 20 
        if len(jogos_disponiveis) < quantidade:
            raise ValueError("Não existem jogos suficientes para gerar a amostra desejadaa.")

        # Seleciona aleatoriamente a quantidade desejada
        amostra = random.sample(jogos_disponiveis, quantidade)

        # Define o caminho do arquivo da amostra
        caminho_amostra = self.caminho_csv.parent / "amostra_steam_games.csv"

        # Grava a amostra em um novo arquivo CSV conforme enunciado
        arquivo_saida = open(caminho_amostra, "w", encoding="utf-8", newline="")

        try:
            # Prepara a gravação dos dados
            gravador = csv.writer(arquivo_saida)

            # Grava o cabeçalho
            gravador.writerow(cabecalho)

            # Grava os 20 jogos selecionados
            gravador.writerows(amostra)

        finally:
            # Garante o fechamento do arquivo
            arquivo_saida.close()

        # Retorna o caminho do arquivo gerado
        return caminho_amostra    
   