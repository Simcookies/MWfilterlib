import math
from math import pi as PI
from .g import butterworth, chebyshey

class BPF:
    def __init__(self, f0, dw, gama = 50):
        self.f0 = f0
        self.w0 = 2*PI*f0*1e9
        self.dw = 2*PI*dw*1e9
        self.gama = gama

    def cal_series(self,g):
        L = 1.0/self.dw*self.gama*g
        C = 1/(math.pow(self.w0,2)*L)
        return round(L*1e9, 3), round(C*1e12, 3)

    def cal_parallel(self,g):
        C = 1.0/(self.dw*self.gama)*g
        L = 1/math.pow(self.w0,2)/C
        return round(L*1e9, 3), round(C*1e12, 3)
