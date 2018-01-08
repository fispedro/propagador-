# -*- coding: utf-8 -*-


#----paquetes mios----
import Data as dt
import fun_proc as fp
import I as it

#===llamadas a metodos====
dt = dt.Data()
fp = fp.Proc()
it = it.I()
#================


datos = dt.read('a.csv')
x = dt.colum_nu(1,datos)
y = dt.colum_nu(0,datos)
pob = dt.colum_nu(2,datos)
xy = dt.une_filas(x,y)
v_int = fp.dis(xy,3)
v_coef = it.coef(pob,v_int,xy)
