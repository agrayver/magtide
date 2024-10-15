import scipy.io as sio
import numpy as np

for c in constituents:
    Br_model = sio.loadmat("./data/MODEL/%s_Br_mod_430km.mat" % c)['B_r_model']
    R_n = sio.loadmat("./data/MODEL/%s_Br_mod_430km.mat" % c)['R_n']
    np.savez_compressed("./data/MODEL/%s_Br_mod_430km" % c, Br_model=Br_model, R_n = R_n)