# -*- coding: utf-8 -*-

import math
from g import butterworth, chebyshey
PI = math.pi

class BSF:
    def __init__(self, f0, FBW, n, G0 = 0.02):
        self.f0  = f0*1e9
        self.w0  = 2*PI*self.f0
        self.FBW = FBW
        self.n   = n
        self.G0  = G0

    def __get_L(self, C):
        L= 1.0/math.pow(self.w0,2)/C
        return L

    def __get_Z(self, L):
        Z = 4*self.w0*L/PI
        return Z

    def get_CLZ(self):
        Cr = Lr = Z = []
        Cr1 = math.pow(J,2)*self.FBW*gi*gj/self.G0/self.w0
        Lr1 = self.__get_L(Cr1)
        Z1  = self.__get_Z(Lr1)
        Cr.append(round(Cr1*1e12,3))
        Lr.append(round(Lr1*1e9,3))
        Z.append(round(Z1,3))

        elif i == self.n:
            Crn = math.pow(J,2)*FBW*gn*gn_next/w0/Gn_next
            Lrn = self.__get_L(Crn)
            return round(Crn*1e12,3), round(Lrn*1e9, 3)
        else:
            pre_Cri = pre_Cri*1e-12
            Cri = math.pow(J*FBW/w0,2)*pre_gi*gi/pre_Cri
            Lri = self.__get_L(Cri)
            Zi  = self.__get_Z(Lri)
            return round(Cri*1e12,3), round(Lri*1e9,3), round(Zi, 3)

f0  = 2    # GHz
FBW = 0.2  # %
bsf = BSF(f0, FBW, 3)
#print(bsf.get_CLZ(3, 1,1.0316,1/30))
#Z01 = 30      # Ohm
#Z02 = 20
#zxZ03 = 20
