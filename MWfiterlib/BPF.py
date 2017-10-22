import math
PI = math.pi

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

f0 = 3.261
BW = 0.5
bpf = BPF(f0, BW)

L1, C1, = bpf.cal_parallel(1)
L2, C2, = bpf.cal_series(2)
L3, C3, = bpf.cal_parallel(1)

print()
print("g1:", L1, "nH", C1, "pF")
print("g2:", L2, "nH", C2, "pF")
print("g3:", L3, "nH", C3, "pF")
