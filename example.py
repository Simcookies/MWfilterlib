from BSF import BSF
f0  = 2    # GHz
FBW = 0.4  # %
n = 5
bsf = BSF(f0, FBW, n, r=0.1)
J0 = 1/43
J1 = 1/43
J2 = 1/43
C, L, Z = bsf.get_CLZ([J0, J1, J2, J2, J1, J0])
print(Z)
