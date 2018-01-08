# -*- coding: utf-8 -*-
import os
from os import listdir
import csv
import numpy as np


class Data:

    def read(self,name):
        with open(name) as csvarchivo:
            entrada=csv.reader(csvarchivo)
            data =[a for a in entrada]
        return data

    def colum_nu(self,no_c,datos):
        fil = np.asarray([float(datos[i][no_c]) for i in range(len(datos))])
        return fil

    def une_filas(self,fila1,fila2):
        uni = np.asarray([[fila1[i],fila2[i]] for i in range(len(fila1))])
        return uni


#data = Data()
#datos = data.read('a.csv')
#x = data.colum_nu(0,datos)
#y = data.colum_nu(1,datos)
#xy = data.une_filas(x,y)
#print len(x),type(xy[0]), x,y,xy
