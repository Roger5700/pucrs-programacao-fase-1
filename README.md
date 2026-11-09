# Projeto PUCRS – Programação para Dados | Fase I

## 1. Apresentação
Este projeto foi desenvolvido como parte da disciplina **Programação para Dados**, da Pontifícia Universidade Católica do Rio Grande do Sul (PUCRS).
O trabalho utiliza uma base de dados da plataforma Steam para realizar análises quantitativas sobre os jogos cadastrados, aplicando conceitos de programação em Python, manipulação de arquivos CSV e Programação Orientada a Objetos.

## 2. Objetivos do projeto
Desenvolver um módulo Python capaz de processar uma base de dados e responder às seguintes questões:
1. Qual é o percentual de jogos gratuitos e pagos na plataforma Steam?
2. Qual é o ano com o maior número de novos jogos? Em caso de empate, retornar uma lista com os anos empatados.
3. Qual é a compatibilidade dos jogos pagos com os sistemas operacionais Windows, Mac e Linux, individualmente e em suas combinações?

## 3. Tecnologias e recursos utilizados
- Python 3.14
- Visual Studio Code
- Biblioteca padrão `csv`
- Biblioteca padrão `pathlib`
- Biblioteca padrão `unittest`
- Biblioteca padrão `tempfile`
- Arquivos CSV
- Excel para cálculos manuais, memória de cálculo e visualização dos resultados.
- Git e GitHub para controle de versão e disponibilização do projeto.

## 4. Estrutura do projeto
- `Fase_I.py`: programa principal responsável pela execução das análises.
- `steam_games.py`: módulo que contém a classe `SteamGames` e os métodos de processamento dos dados.
- `testes.py`: módulo responsável pelos testes automatizados.
- `steam_games.csv`: base completa de dados.
- `amostra_steam_games.csv`: amostra de 20 jogos utilizada na validação dos resultados.

## 5. Metodologia
As análises foram realizadas utilizando a base completa da Steam, composta por 72.934 registros e 39 colunas.
Para validar os métodos desenvolvidos, foi selecionada uma amostra aleatória de 20 jogos, armazenada em um arquivo CSV independente.
Os resultados esperados dos testes foram calculados manualmente utilizando o Microsoft Excel e posteriormente comparados com os resultados obtidos pelo Python.

## 6. Testes automatizados
Foi utilizada a biblioteca nativa `unittest` para verificar os resultados dos métodos desenvolvidos.
Os testes contemplam:
- Verificação da quantidade e do percentual de jogos gratuitos e pagos.
- Identificação do ano com maior quantidade de lançamentos.
- Verificação do tratamento de empate entre anos.
- Análise da compatibilidade dos sistemas operacionais.

## 7. Arquivos Complementares 
- Relatório final em Word contendo as análises e conclusões dos resultados.
- O arquivo em Excel, contendo a amostra de 20 jogos, a memória de cálculo e o Dashboard.
Esses documentos apresentam as análises conclusivas das informações processadas pelo programa.

## 8. Como executar o projeto

Para executar o projeto, certifique-se de que o Python esteja instalado e que os arquivos necessários estejam organizados na mesma estrutura de diretórios.

**Para executar o programa principal:**

```bash
python Fase_I.py
```

**Para executar os testes automatizados:**

```bash
python testes.py
```


## 9. Resultados da validação
Os testes automatizados foram executados com sucesso, apresentando quatro testes aprovados (`OK`).
Os resultados da amostra foram comparados com os cálculos manuais realizados no Excel.

## 10. Considerações finais
O projeto permitiu aplicar conceitos fundamentais de programação para dados, incluindo leitura e processamento de arquivos CSV, manipulação de estruturas de dados, tratamento de exceções, desenvolvimento de classes e métodos, além da implementação de testes automatizados. O desenvolvimento também proporcionou a integração entre Python e Excel como ferramentas complementares para análise e validação de dados.

**Instituição:** Pontifícia Universidade Católica do Rio Grande do Sul (PUCRS)  
**Disciplina:** Programação para Dados  
**Trabalho:** Fase I

**Professor:** Marco Aurélio Souza Mangan
