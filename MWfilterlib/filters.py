import math
from math import pi as PI
from .tools import chebyshey


class LPF:
    '''
    fc:   center frequency (GHz)
    gama: default is 50
    '''
    def __init__(self, fc, gama=50):
        self.fc = fc
        self.wc = 2 * PI * fc * 1e9
        self.gama = gama

    def cal_L(self, g):
        L = 1.0 / self.wc * self.gama * g
        return round(L * 1e9, 3)

    def cal_C(self, g):
        C = 1.0 / self.wc * g / self.gama
        return round(C * 1e12, 3)


class HPF:
    '''
    fc:   center frequency (GHz)
    gama: default is 50
    '''
    def __init__(self, fc, gama=50):
        self.fc = fc
        self.wc = 2 * PI * fc * 1e9
        self.gama = gama


class BPF:
    def __init__(self, f0, dw, gama=50):
        self.f0 = f0
        self.w0 = 2 * PI * f0 * 1e9
        self.dw = 2 * PI * dw * 1e9
        self.gama = gama

    def cal_series(self, g):
        L = 1.0 / self.dw * self.gama * g
        C = 1 / (math.pow(self.w0, 2) * L)
        return round(L * 1e9, 3), round(C * 1e12, 3)

    def cal_parallel(self, g):
        C = 1.0 / (self.dw * self.gama) * g
        L = 1 / math.pow(self.w0, 2) / C
        return round(L * 1e9, 3), round(C * 1e12, 3)


class BSF:
    # initialize class.
    #   f0:  center frequency (GHz)
    #   FBW: frac-bandwidth
    #   n:   order of filter
    #  (r):  ripple of chebyshey filter (dB), default value 0.1dB
    #  (G0): input admittance, default value 0.02S
    #  (Gn1):output admittance, default value 0.02S
    def __init__(self, f0, FBW, n, r=0.1, G0=0.02, Gn1=0.02):
        self.f0 = f0 * 1e9
        self.w0 = 2 * PI * self.f0
        self.FBW = FBW
        self.n = n
        self.G0 = G0
        self.Gn1 = Gn1
        self.r = r

    # private method
    def __get_C(self, L):
        return 1 / math.pow(self.w0, 2) / L

    def __get_L(self, C):
        return 1 / math.pow(self.w0, 2) / C

    def __get_Z(self, L):
        return 4 * self.w0 * L / PI

    # public method
    def get_CLZ(self, J):
        Cr = []
        Lr = []
        Zr = []
        g = chebyshey(self.n, self.r)

        # Cr1 calced by J01(J[0])
        Cr1 = math.pow(J[0], 2) * self.FBW * g[0] * g[1] / self.G0 / self.w0
        Lr1 = self.__get_L(Cr1)
        Zr1 = self.__get_Z(Lr1)
        Cr.append(round(Cr1 * 1e12, 3))
        Lr.append(round(Lr1 * 1e9, 3))
        Zr.append(round(Zr1, 3))

        temp_Cri = Cr1
        # Cr,i+1(1<i<n-1) calced by Ji,i+1(J[i])
        for i in range(1, self.n - 1):
            temp_Cri = math.pow(J[i] * self.FBW / self.w0,
                                2) * g[i] * g[i + 1] / temp_Cri
            Cri1 = temp_Cri
            Lri1 = self.__get_L(Cri1)
            Zri1 = self.__get_Z(Lri1)
            Cr.append(round(Cri1 * 1e12, 3))
            Lr.append(round(Lri1 * 1e9, 3))
            Zr.append(round(Zri1, 3))

        # Crn calced by Jn,n+1(J[n])
        Crn = math.pow(
            J[self.n],
            2) * self.FBW * g[self.n] * g[self.n + 1] / self.w0 / self.G0
        Lrn = self.__get_L(Crn)
        Zrn = self.__get_Z(Lrn)
        Cr.append(round(Crn * 1e12, 3))
        Lr.append(round(Lrn * 1e9, 3))
        Zr.append(round(Zrn, 3))
        return Cr, Lr, Zr
