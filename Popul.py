#####################################################
# Sistemas Inteligentes em Bioinformática 2019/2020 #
# Traveller salesman problem solver                 #
# Authors                                           #
# - Bruno Pereira                                   #
# - David Santos                                    #
# - Mário Varela                                    #
# - Rui Pires                                       #
#####################################################

from Indiv import Indiv, IndivPermut
from random import random, uniform
import numpy as np

class Popul:

    def __init__(self, popsize, indsize, indivs = []):
        self.popsize = popsize
        self.indsize = indsize
        if indivs: self.indivs = indivs
        else: self.initRandomPop()

    def getIndiv(self, index):
        return self.indivs[index]

    def initRandomPop(self):
        self.indivs = []
        for i in range(self.popsize):
            indiv_i = Indiv(self.indsize, [])
            self.indivs.append(indiv_i)

    def getFitnesses(self):
        fitnesses = []
        for ind in self.indivs:
            fitnesses.append(ind.getFitness())
        return fitnesses
        
    def bestFitness(self):
        return max(self.getFitnesses())

    def bestSolution(self):
        fitnesses = self.getFitnesses()
        bestf = fitnesses[0]
        bestsol = 0.0
        for i in range(1,len(fitnesses)):
            if fitnesses[i] > bestf:
                bestf = fitnesses[i]
                bestsol = i
        return self.getIndiv(bestsol), bestf
    
    def selection(self, n):
        res = []
        #fitnesses = list(self.linscaling(self.getFitnesses()))
        fitnesses = list(self.getFitnesses())
        for i in range(n):
            sel = self.roulette(fitnesses)
            fitnesses[sel] = 0.0
            res.append(sel)
        return res
    
    def roulette(self, f):
        tot = sum(f)
        val = uniform(0.75,1)
        acum = 0.0
        ind = 0
        while acum < val:
            acum += (f[ind] / tot)
            ind += 1
        return ind-1
    
    def linscaling(self, fitnesses):
        mx = max(fitnesses)
        mn = min(fitnesses)
        res = []
        for f in fitnesses:
            val = (f-mn)/(mx-mn)
            res.append(val)
        return res
    
    def recombination(self, parents, noffspring):
        offspring = []
        new_inds = 0
        while new_inds < noffspring:
            parent1 = self.indivs[parents[new_inds]]
            parent2 = self.indivs[parents[new_inds+1]]
            offsp1, offsp2 = parent1.crossover(parent2)
            offsp1.mutation()
            offsp2.mutation()
            offspring.append(offsp1)
            offspring.append(offsp2)
            new_inds += 2
        return offspring
       
    def reinsertion(self, offspring):
        tokeep = self.selection(self.popsize-len(offspring))
        ind_offsp = 0
        for i in range(self.popsize):
            if i not in tokeep:
                self.indivs[i] = offspring[ind_offsp]
                ind_offsp += 1
        


class PopulPermut(Popul):
    
    def __init__(self, popsize, indsize, indivs = []):
        self.popsize = popsize
        self.indsize = indsize
        if indivs: self.indivs = indivs
        else: self.initRandomPopPer()
    
    #gera uma população nova
    def initRandomPopPer(self):
        self.indivs = []
        for i in range(self.popsize):
            indiv_i = IndivPermut(self.indsize)
            self.indivs.append(indiv_i)
            
    
    def bestFitness(self):
        return min(self.getFitnesses())

    #melhor individuo com a fitness mais baixa
    def bestSolution(self):
        fitnesses = self.getFitnesses()
        bestf = fitnesses[0]
        bestsol = 0
        for i in range(1,len(fitnesses)):
            if fitnesses[i] < bestf:
                bestf = fitnesses[i]
                bestsol = i
        return self.getIndiv(bestsol), bestf
    
    #seleção feita de acordo com o ranking, os melhores são os escolhidos
    def selection(self, n):
        res = []
        #fitnesses = list(self.linscaling(self.getFitnesses()))
        fitnesses = list(self.getFitnesses())
        for i in range(n):
            sel = fitnesses.index(min(fitnesses))
            fitnesses[sel] = 9999999999999999999999
            res.append(sel)
        return res

    #método para gerar os filhos a partir dos pais  
    def recombination(self, parents, noffspring,cl=False):
        offspring = []
        new_inds = 0
        while new_inds < noffspring:
            parent1 = self.indivs[parents[new_inds]]
            parent2 = self.indivs[parents[new_inds+1]]
            offsp1, offsp2 = parent1.crossover(parent2,cl)
            offsp1.mutation()
            offsp2.mutation()
            offspring.append(offsp1)
            offspring.append(offsp2)
            new_inds += 2
        return offspring
    
    #método para realizar a nova geração
    #incorpora os filhos numa população onde são mantidos os n melhores
    def reinsertion(self, offspring):   
        tokeep = self.selection(self.popsize-len(offspring))
        ind_offsp = 0
        for i in range(self.popsize):
            if i not in tokeep:
                self.indivs[i] = offspring[ind_offsp]
                ind_offsp += 1


    
