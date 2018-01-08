# -*- coding: utf-8 -*-
import numpy as np

class I:

    def coef(self,pob,v_int,xy):#vector de coeficientes
        v_coef = []
        for i,v in enumerate(v_int):
            int_ij = []
            for j in v:
                n = pob[i]*pob[j]
                int_ij.append(n)
            v_coef.append(np.asarray(int_ij))
            int_ij = []

    def coef2(self,pob,v_int,xy):#vector de coeficientes
        v_coef = []
        g=[]
        xy=np.asarray(xy)

        for i,v in enumerate(v_int):
            v_ii=[]
            v_dd=[]
            p_c=[]
            s_p=0
            s_d=0
            for j in v:
                s_p = pob[j]+s_p
                dif=xy[i]-xy[j]
                s_d= s_d+(1/np.dot(dif,dif))
            s_d=1/s_d
            for l in v:
                v_ii.append(pob[l]/s_p)
                dif=xy[i]-xy[l]
                v_dd.append(s_d/np.dot(dif,dif))
            for k,v in enumerate(v_ii):
                pc=v_dd[k]*v
                p_c.append(pc)#cambiar por pc
            p_c=np.asarray(p_c)
            v_coef.append(p_c)
            a=reduce(lambda x,y: x+y,p_c)
            g.append(a)
        v_coef=np.asarray(v_coef)
        s_pp=100/(reduce(lambda x,y: x+y,pob))
        return v_coef
