import math
PI = math.pi

class LPF:
    def __init__(self, fc, gama = 50):
        self.fc = fc
        self.wc = 2*PI*fc*1e9
        self.gama = gama

    def cal_L(self,g):
        L = 1.0/self.wc*self.gama*g
        return round(L*1e9, 3)

    def cal_C(self,g):
        C = 1.0/self.wc*g/self.gama
        return round(C*1e12, 3)

lpf = LPF(3.260)

print()
print(lpf.cal_L(2), "nH")
print(lpf.cal_C(1), "pF")