# -*- coding: utf-8 -*-
import numpy as np

class Proc:

    def dis(self,xy,n_im):
        aaa =[]
        for x in xy:
            dis=[np.dot(x-y,x-y) for y in xy]
            dis2 = sorted(dis)
            aa = []
            for i in range(1,(n_im+1)):
                a = dis.index(dis2[i])
                aa.append(a)
            aaa.append(aa)

        for j in range(len(aaa)):
            for i in range((n_im)):
                aaa[aaa[j][i]].append(j)
        v_int = np.asarray([np.asarray(list(set(i))) for i in aaa])
        return v_int
