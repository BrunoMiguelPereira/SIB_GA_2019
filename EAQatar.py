#####################################################
# Sistemas Inteligentes em Bioinformática 2019/2020 #
# Traveller salesman problem solver                 #
# Authors                                           #
# - Bruno Pereira                                   #
# - David Santos                                    #
# - Mário Varela                                    #
# - Rui Pires                                       #
#####################################################
from EvolAlgorithm import EvolAlgorithm
from Popul import  PopulPermut
from math import sqrt as sq

#Ler o ficheiro com os dados das cidades
def read_file(filename):
    try:
        cities = {}
        with open(filename,"r") as file:
            lines = file.readlines()
            dim = lines[4].rstrip().split()[2]
            for i in range(7,len(lines)-1):
                line = lines[i].rstrip().split()
                cities[int(line[0])] = (float(line[1]),float(line[2]))
            file.close()
        return cities,dim
    except IOError:
        print("Ficheiro não encontrado.")
    else:
        print("Ficheiro lido com sucesso.\n")

#Função para calcular a distânica (euclidiana)      
def distancia(a,b):
    return sq((a[0]-b[0])**2 + (a[1]-b[1])**2)
  
#Armazenar e devolver um dicionario de dicionários
#cidade1 -> {cidade2:dist}      
def distance_matrix(dicionario):
    D = {}
    for city1,cords1 in dicionario.items():
        D[city1] = {}
        for city2,cords2 in dicionario.items():
            D[city1][city2] = distancia(cords1,cords2)
    return D



class EvoQatar(EvolAlgorithm):
    
    #inicializar a classe para o problema
    def __init__(self,popsize,numits,noffspring,indsize,dist_matrix):
        self.popsize = popsize
        self.numits = numits
        self.noffspring = noffspring
        self.indsize = indsize
        self.dist_matrix = dist_matrix
    
    #inicializar a população com representação permutável aleatoriamente
    def initPopul(self, indsize):
        self.popul = PopulPermut(self.popsize, indsize)
    
    #faz uma geração, seleciona os pais, gera os filhos sendo que há thresholds 
    #que alteram a forma como os filhos são gerados para quebrar uma população
    #idêntica
    def iteration(self):
        parents = self.popul.selection(self.noffspring)
        if not self.popul.bestFitness()>20000:
            offspring = self.popul.recombination(parents, self.noffspring)
            self.evaluate(offspring)
        elif 15000<self.popul.bestFitness()<20000:
            offspring = self.popul.recombination(parents, self.noffspring,True)
            self.evaluate(offspring)
        elif self.popul.bestFitness()<15000:
            offspring = self.popul.recombination(parents, self.noffspring)
            self.evaluate(offspring)
        else:
            offspring = self.popul.recombination(parents, self.noffspring,True)
            self.evaluate(offspring)
        self.popul.reinsertion(offspring)
    
    #estabelece a fitness para um conjunto dos indivíduos
    def evaluate(self,indivs):
        for i in range(len(indivs)):
            ind = indivs[i]
            fit = 0.0
            genes = ind.getGenes()
            for i in range(0,len(genes)-1):
                fit += self.dist_matrix[genes[i]][genes[i+1]]
            ind.setFitness(fit)
        return None
    
    
    #corre o algoritmo evolucionário
    def run(self):
        self.initPopul(self.indsize)
        self.evaluate(self.popul.indivs)
        self.bestsol = []
        self.bestfit = 99999999999999999999
        for i in range(self.numits+1):            
            self.iteration()
            bs, bf = self.popul.bestSolution()
            if bf < self.bestfit:
                self.bestfit = bf
                self.bestsol = bs
            print("Iteration:", i, " ", "Best: ", self.popul.bestFitness())

    
    def printBestSolution(self):
        print("Best solution: ", self.bestsol.getGenes())
        print("Best fitness:", self.bestfit)


def menu():
    objeto = None
    ind_dim = 0
    pop_size = 50
    n_offsp = 26
    max_iterations = 1000
    matriz = None
    while True:
        print('''\nBem-vindo ao algorítmo genético com o objetivo de encontrar o caminho mais curto que atravessa todas as cidades de um país apenas 1x.
        Disponibilizamos as seguintes opções:
                  1. Ler o ficheiro com a informação do país (TSPLIB Format)
                  2. Ler parâmetros para correr o algoritmo genético (se não quiser modificar corra o algoritmo)
                  3. Correr algoritmo genético
                  4. Sair''')
        op = input("Opção pretendida? ")
        if op == "1":
            try:
                filename = input("Nome do ficheiro a analisar (não se esqueça da extensão): ")
                cidades,dim = read_file(filename)
                ind_dim = int(dim)+1
                matriz = distance_matrix(cidades)
            except:
                raise
            else:
                print("\nFicheiro lido com sucesso.\n")
        elif op == "2":
            try:
                popsize_i = int(input("Tamanho da população (Enter para default)? "))
            except ValueError:
                pop_size = 50
            else:
                pop_size = popsize_i
            try:
                n_offspring = int(input("Número de filhos por geração (Enter para default)? "))
            except ValueError:
                n_offsp = 26
            else:
                n_offsp = n_offspring
            try:
                n_iter = int(input("Número de iterações de todo o processo a realizar (Enter para default)? "))
            except ValueError:
                max_iterations = 1000
            else:
                max_iterations = n_iter
        elif op == "3":
            objeto = EvoQatar(pop_size,max_iterations,n_offsp,ind_dim,matriz)
            objeto.run()
            objeto.printBestSolution()            
        elif op == "4":
            break
    print("Adeus, Obrigado!")
                
            
            
            
            
        
if __name__=="__main__":
    menu()




    
    

