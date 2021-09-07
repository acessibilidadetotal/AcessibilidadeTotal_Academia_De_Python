from No import No
from DateModel import *

class DataFestiva(DataModel):
    
    def __init__(self, day, month, yer):
        super().__init__(day, month, yer)
        self.inicio = None
        self.tamanho = 0

    def adicionar(self, data):
        if self.inicio:
            data = self.inicio
            while (data.proximo):
                data = data.proximo
                data.proximo = No(data)
            else:
                self.inicio = No(data)
                self.tamanho += 1

    def imprimir(self): 
        if( self.inicio == None ) :
            print( "Lista Vazia!!")
        else:
            data = self.inicio
            while ( data ):
                print( data.data, "\n")
                data = data.proximo
            print("Tamanho da lista: ", self.tamanho)
            print("--------------------------")
            