import numpy as np

class Ferramenta:
    
    def __init__(self,input):

        self.input = input
        self.matriz = []
        self.b = []
        self.resultadocramer = []

        self.resultados(input)
        self.determinante(self.matriz)
        self.inversa(self.matriz)
        self.cramer(self.matriz)


    def resultados(self, input):

        for i in input:
            ultimo = i.pop()
            self.b.append(ultimo)
            self.matriz = input

    def determinante(self,matriz):
        det = round(np.linalg.det(matriz))
        self.det = det   


    def cramer(self,matriz):
        
        detC = []
        i = 0

        while i < 3:
            matriz = np.copy(self.matriz)
            b = np.copy(self.b)

            matriz[0][i] = b[0]
            matriz[1][i] = b[1]
            matriz[2][i] = b[2]

            detC = np.linalg.det(matriz)
            a = round(detC/self.det)
            self.resultadocramer.append([a])
            i += 1
    
    def inversa(self,matriz):
        inv = []
        inv = np.linalg.inv(matriz)
        #self.inv = inv
        self.resultadoinv = np.dot(inv,self.b)