import sys
import os
import shutil
import numpy as np

if len(sys.argv) < 3:
    print "Need three parameters!"
else: 
    t0 = int(sys.argv[1])
    t1 = int(sys.argv[2])
    nt = int(sys.argv[3])
    if not os.path.exists("wf"):
        os.mkdir("wf")

    data = np.linspace(t0, t1, nt)
    for i in data:
        fname = "POSCAR_%06d"%int(i)
        shutil.copy(fname, "wf")
