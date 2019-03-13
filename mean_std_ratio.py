import numpy as np
import os
import pylab as plt
from scipy import interpolate
from scipy.interpolate import UnivariateSpline
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter

def output_data(flexdeoutputfile,name):
    with open(flexdeoutputfile,'r') as f:
        content=f.readlines()
        values=[]
        coordinates=[]
        for line in content:
            if len(line) > 2:
                if "VAL({}".format(name) in line:
                    values.append(float(line.split()[1]))
                    coordinates.append(str(line.split()[0].split("VAL")[1]))
        values=np.array(values)
        coordinates=np.array(coordinates)
        values=values.reshape(5,5,5,8)
        coordinates=coordinates.reshape(5,5,5,8)
        std_z=[]
        for x in range(0,5):
            for y in range(0,5):
                for i in range(0,4):
                    column_z=[]
                    for k in [i,i+4]:
                        for z in range(0,5):
                            column_z.append(values[z][y][x][k])
                    std_z.append(np.std(column_z))
        std_x=[]
        for y in range(0,5):
            for z in range(0,5):
                for i in range(0,4):
                    column_x=[]
                    for k in [i,i+1]:
                        for x in range(0,5):
                            column_x.append(values[z][y][x][k])
                    std_x.append(np.std(column_x))
        return np.mean(std_z)/np.mean(std_x)
t,p=np.loadtxt('/nfshome/khachaturyan/Publication/3D_cube/cube_simulation/calculated/Ortho_cor/Ortho.p01', unpack=True)

polarization=[]
value=[]
for i in range(1,14):
    path="/nfshome/khachaturyan/Publication/3D_cube/cube_simulation/calculated/Ortho_cor/E_P_cor_{}.out".format(i)
    value.append(100*output_data(path,"xcomp"))
    with open("/nfshome/khachaturyan/Publication/3D_cube/cube_simulation/calculated/Ortho_cor/E_P_cor_{}.out".format(i),"r") as f:
        content=f.readlines()
        for line in content:
            if "Time" in line:
                t_n=float(line.split(' ')[-1])
    p_n=round(p[np.where(t==t_n)][0],3)
    polarization.append(p_n)
plt.plot(polarization,value)
plt.savefig("/nfshome/khachaturyan/Publication/3D_cube/cube_simulation/cor_pic/Ex.jpg",dpi=1200, bbox_inches="tight")
plt.show()