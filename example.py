from MWfilterlib import BSF, BPF, LPF
# f0  = 2    # GHz
# FBW = 0.4  # %
# n = 5
# bsf = BSF(f0, FBW, n, r=0.1)
# J0 = 1/43
# J1 = 1/43
# J2 = 1/43
# C, L, Z = bsf.get_CLZ([J0, J1, J2, J2, J1, J0])
# print(Z)


f0 = 1.8
BW = 0.02
bpf = BPF(f0, BW)

L1, C1, = bpf.cal_parallel(1)
L2, C2, = bpf.cal_series(2)
L3, C3, = bpf.cal_parallel(1)

print()
print("g1:", L1, "nH", C1, "pF")
print("g2:", L2, "nH", C2, "pF")
print("g3:", L3, "nH", C3, "pF")

lpf = LPF(3.260)

# print()
# print(lpf.cal_L(2), "nH")
# print(lpf.cal_C(1), "pF")
