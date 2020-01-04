#####################################################
# Sistemas Inteligentes em Bioinformática 2019/2020 #
# Traveller salesman problem solver                 #
# Authors                                           #
# - Bruno Pereira                                   #
# - David Santos                                    #
# - Mário Varela                                    #
# - Rui Pires                                       #
#####################################################

from random import randint, random, shuffle, choice
import numpy as np




class Indiv:
    
    def __init__(self, size, genes = []):
        if genes: self.genes = genes 
        else: self.initRandom(size)
        self.fitness = None
        
    def setFitness(self, fit):
        self.fitness = fit

    def getFitness(self):
        return self.fitness
    
    def getGenes(self):
        return self.genes
    
    def initRandom(self, size):
        self.genes = []
        for i in range(size):
            self.genes.append(randint(0,1))
            
    def mutation(self):
        s = len(self.genes)
        pos = randint(0,s-1)
        if self.genes[pos] == 0: self.genes[pos] = 1
        else: self.genes[pos] = 0
    
    def crossover(self, indiv2):
        return self.one_pt_crossover(indiv2)
    
    def one_pt_crossover(self, indiv2):
        offsp1 = []
        offsp2 = []
        s = len(self.genes)
        pos = randint(0,s-1)
        for i in range(pos):
            offsp1.append(self.genes[i])
            offsp2.append(indiv2.genes[i])
        for i in range(pos, s):
            offsp2.append(self.genes[i])
            offsp1.append(indiv2.genes[i])
        return Indiv(s, offsp1), Indiv(s, offsp2)
    


class IndivPermut (Indiv):

    def __init__(self, size = 195, genes = []):
        self.size = size
        if genes: self.genes = genes
        else: self.initRandomPer()
        self.fitness = None
    
    def initRandomPer(self):
        genes = np.random.permutation(self.size)
        self.genes = genes[genes != 0].tolist()
        return self.genes
        
    #mutação para causar variabilidade, troca de 2 cidades de posição
    def mutation(self):
        nind = len(self.genes)
        i = 0
        j = 0
        while i==j:
            i = randint(0,nind-1)
            j = randint(0,nind-1)
        temp = self.genes[i]
        self.genes[i] = self.genes[j]
        self.genes[j] = temp
        

    
    def crossover(self, indiv2,cl=False):
        return self.one_pt_crossover(indiv2,cl)
    
    #método para realizar o cruzamento de filhos
    #utiliza o parâmetro cl para causar uma mutação maior nos filhos
    def one_pt_crossover(self,indiv2,cl=False):
        s = len(self.genes)
        pos = randint(0,s-1)
        offsp1 = list(self.getGenes())
        offsp2 = list(indiv2.getGenes())
        if not cl:
            offsp1[pos:] = sorted(offsp1[pos:],key=lambda x:indiv2.genes)
            offsp2[pos:] = sorted(offsp2[pos:],key=lambda x:self.genes)
        else:
            l = [True,False]
            ck = choice(l)
            if not ck:
                offsp1[pos:] = sorted(offsp1[pos:])
                offsp2[:pos] = sorted(offsp2[:pos],reverse=True)
            else:
                offsp2[pos:] = sorted(offsp2[pos:])
                offsp1[:pos] = sorted(offsp1[:pos],reverse=True)

        return IndivPermut(s, offsp1), IndivPermut(s, offsp2)
    



