import numpy as np
import matplotlib.pylab as plt

name="Ortho"
if name=="Tetra":
    ps_max=0.3641
elif name=="Rhombo":
    ps_max=0.445
else:
    ps_max=0.42
P=[]
sigma_x=[]
sigma_y=[]
sigma_z=[]
p_val=[]
sigma=[]
t,p=np.loadtxt('/nfshome/khachaturyan/Publication/3D_cube/cube_simulation/calculated/{}/SD/sigma/P_t.p01'.format(name), unpack=True)
for i in [i for i in range(1,2)]:
    i=700
    P=[]
    sigma_x=[]
    sigma_y=[]
    sigma_z=[]
    with open("/nfshome/khachaturyan/Publication/3D_cube/cube_simulation/calculated/{}/SD/sigma/sigma_xyz_{}.out".format(name,i),"r") as f:
        content=f.readlines()
        for line in content:
            if "SURF_INTEGRAL" in line and "x_" in line:
                sigma_x.append(float(line.split('=')[-1]))
            elif "SURF_INTEGRAL" in line and "y_" in line:
                sigma_y.append(float(line.split('=')[-1]))
            elif "SURF_INTEGRAL" in line and "x_" not in line and "y_" not in line :
                sigma_z.append(float(line.split('=')[-1]))
            elif "Time" in line:
                tc=float(line.split(' ')[-1])
                #p_val.append(round(p[np.where(t==tc)][0]/75*2-0.81,2))
                p_val.append(round(p[np.where(t==tc)][0],2))

    sigma_z=np.array(sigma_z)/1e-12
    sigma_x=np.array(sigma_x)/1e-12
    sigma_y=np.array(sigma_y)/1e-12
    '''
    print "sigma_x",np.std(sigma_x)/0.436
    print "sigma_y",np.std(sigma_y)/0.436
    print "sigma_z",np.std(sigma_z)/0.436
    print float(line.split(' ')[-1])
    '''
    sigma.append(np.std(sigma_x)/0.42)
    print (np.std(sigma_x)/ps_max)
    print (np.std(sigma_z)/ps_max)
with open("/nfshome/khachaturyan/Publication/3D_cube/cube_simulation/distributions/field_distributions/calculated/<sigmax>{}.txt".format(name),'w') as f:
    c=zip(p_val,sigma)
    for i in c:
        f.write("{}    {}\n".format(i[0],i[1]))
    f.close()
"""
fig, a = plt.subplots(figsize=(25, 20))
a.plot(p_val,sigma, linewidth=6.0)
a.legend(loc=2,fontsize=45);
a.set_ylabel(r'$\sigma_x$',fontsize=60, x=5)
a.set_xlabel('P, C/m$^{2}$',fontsize=60)
#a.set_xlim(10**-6,1)
#a.set_xscale('log')
#plt.xticks(np.array([10**-5, 1e-3, 1e-1, 10]), y=-0.01)
#a.set_ylim(0.15, 0.5)
#plt.yticks(np.linspace(0.15, 0.5, 8), x=-0.01)
plt.tick_params(labelsize=45)
plt.savefig("sigma_x_{}.jpg".format(name),format='jpg',dpi=300)
"""
"""
m="z"
time=[]
p_val=[]
sigma=[]
t,p=np.loadtxt('/nfshome/khachaturyan/Publication/3D_cube/cube_simulation/calculated/Ortho/field_dist/P_t.p01', unpack=True)
for i in range(1,34):
    d_E=[]
    with open ('/nfshome/khachaturyan/Publication/3D_cube/cube_simulation/calculated/Ortho/field_dist/row/E{}_{}.txt'.format(m,i), 'r') as f:
        s=0
        for line in f:
            s+=1
            a=line.strip()
            if s==5:
                #time.append(float(line.split(' ')[-1]))
                tc=float(line.split(' ')[-1])
                p_val.append(round(p[np.where(t==tc)][0],2))
            if s>7:
                d_E.append(float(a))
    sigma.append(np.std(d_E)/1e6)

with open("/nfshome/khachaturyan/Publication/3D_cube/cube_simulation/distributions/field_distributions/calculated/SD_e{}_ortho.txt".format(m),"w") as f:
    for i,j in zip(p_val,sigma):
        f.write("{} {}\n".format(i,j))
    f.close()
fig, a = plt.subplots(figsize=(25, 20))
a.plot(p_val,sigma, linewidth=6.0)
a.legend(loc=2,fontsize=45);
a.set_ylabel(r'$\sqrt{\langle \vartriangle Ez^{2}\rangle}$, V/m',fontsize=60, x=5)
a.set_xlabel('$P/P_s$',fontsize=60)
a.set_xlim(-1,1)
#a.set_xscale('log')
#plt.xticks(np.array([]), y=-0.01)
a.set_ylim(0.05, 0.08)
plt.yticks(np.linspace(0.05, 0.08, 6), x=-0.01)
plt.tick_params(labelsize=45)
plt.savefig("/nfshome/khachaturyan/Publication/3D_cube/cube_simulation/distributions/field_distributions/calculated/<E_{}>.jpg".format(m),format='jpg',dpi=300)
"""
"""
#for virgine
d_E=[]
with open ('/nfshome/khachaturyan/Publication/3D_cube/cube_simulation/distributions/field_distributions/data/Ex.txt', 'r') as f:
    s=0
    for line in f:
        s+=1
        a=line.strip()
        if s>7:
            d_E.append(float(a))
print (np.std(d_E)/1e6)
"""