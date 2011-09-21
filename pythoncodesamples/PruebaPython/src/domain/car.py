'''
Created on 20/09/2011

@author: pmartinez
'''

class CompactCar(object):
    '''
    classdocs
    '''
  
    def __init__(self,pmarca,pmodelo,panio):
        '''
        Constructor
        '''
        self.marca = pmarca
        self.modelo = pmodelo
        self.anio = panio
        
    def ver_marca(self):
        print self.marca
    def ver_modelo(self):
        print self.modelo
    def ver_anio(self):
        print self.anio
    def tostring(self):
        print "La marca es: " + self.marca + " modelo: "+self.modelo +" Anio: " +self.anio
        
        