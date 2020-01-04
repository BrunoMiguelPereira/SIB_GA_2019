# SIB_GA_2019
Trabalho de Sistemas Inteligentes para Bioinformática

O algoritmo genético está ao todo divido por 4 módulos. Surge de um adaptação dos algoritmos genéticos já leccionados no mestrado de Bioinformática da Universidade do Minho.

Módulo Indiv: Módulo que compreende um indivíduo da população. Classe Indiv (para um algoritmo genético (AG) geral) e outra (IndivPermut) para o problema em questão. IndivPermut contém métodos específicos como operador de mutação para representações de permutações e o crossover com preservação de ordem.

Módulo Popul: Módulo que compreende uma população de um AG. Classe Popul (para um AG geral) e outra (PopulPermut) que se adequa ao problema em questão. Método de seleção é realizado pela ordem.

Módulo EvolAlgorithm: É a classe que contém a estrutura base de um algoritmo genético, não específico.

Módulo EAQatar: Módulo com os métodos implementados para resolver o problema do "caixeiro viajante" para um determinado país utilizando algoritmos genéticos. Necessita de um ficheiro para construir a matriz de distância que está gravada como um dicionário de dicionários. O utilizador pode sempre alterar os parâmetros do algoritmo que neste caso são: o tamanho da população, o número de filhos por geração e o número de iterações do algoritmo. O progama está implementado como um menu onde o utilizador poderá sempre ler diferentes ficheiros e alterar os parâmetros.

#Notas: 
Os nossos resultados não são ótimos globais quando corremos o algoritmo um número de vezes suficientemente alto. 
Um resultado na ordem dos 15000 é obtido como um ótimo local. 
Tentámos quebrar este ponto de convergência com um método de seleção dos pais diferente a partir de um determinado threshold o que não resultou.
Num futuro trabalho deveria ser considerado aumentar a taxa de mutação por iteração, bem como mutações mais eficientes, ou implementar métodos de seleção diferentes, por exemplo o torneio.

