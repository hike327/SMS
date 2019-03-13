import numpy as np
import os
import pylab as plt

name="Ep"

def data_read(name,step):
    values=[]
    with open ('/nfshome/khachaturyan/Publication/3D_cube/cube_simulation/distributions/field_distributions/data/{}_{}.txt'.format(name,step), 'r') as f:
            s=0
            for line in f:
                s+=1
                a=line.strip()
                if s>7:
                    values.append(float(a))
    return (np.array(values)-np.array(np.mean(values)))/1.8e6

def XY(x,y):
    return np.mean(x*y)

path_to_data="/nfshome/khachaturyan/Publication/3D_cube/cube_simulation/distributions/field_distributions/data/"
time_steps=[]
polarization=[]
step=[]
name2="EpEp"
name1="EpEv"

for file in os.listdir('{}'.format(path_to_data)):
    if file.endswith(".txt") and name in file:
        with open (path_to_data+file, "r") as f:
            a=f.readlines()
            time_steps.append(float(a[4].split(" ")[-1]))
        if int(file.split("_")[1].split(".")[0]) not in step:
            step.append(int(file.split("_")[1].split(".")[0]))

step=sorted(np.array(step))
time_steps=sorted(np.array(time_steps))
p_values=[]
t,p=np.loadtxt('{}P_t.p01'.format(path_to_data), unpack=True)
print (np.shape(p))
for s in time_steps:
    print (s)
    #print (s, round(p[np.where(t==s)][0],3))
    p_values.append(round(p[np.where(t==s)][0],3))

cor_val0=[]
cor_val1=[]
cor_val2=[]
ev=data_read("Ev",2)
ev_xy=XY(ev,ev)
for i in (step):
    ep=data_read(name,i)
    cor_val1.append(XY(ep,ep))
    cor_val2.append(2*XY(ep,ev))
    cor_val0.append(ev_xy)

cor_val1=np.array(cor_val1)
cor_val2=np.array(cor_val2)
cor_val0=np.array(cor_val0)

plt.plot(p_values,cor_val1,p_values,cor_val2,p_values,cor_val1+cor_val2)#np.sqrt(1+cor_val0+cor_val1+cor_val2))
plt.show()
#plt.xlim(-0.8,0.8)
#plt.ylim(-2.2, 1.7)
plt.savefig("epep-2epev.jpg".format(name1))

"""
#try to replace it by cov
np.cov(x,y)
"""
"""
def cor_func(name,step,time):
    values=[]
    with open ('/nfshome/khachaturyan/Publication/3D_cube/cube_simulation/cube/{}_{}.txt'.format(name,step), 'r') as f:
            s=0
            for line in f:
                s+=1
                a=line.strip()
                if s>7:
                    values.append(float(a))
    return np.mean(values)

path_to_data="/nfshome/khachaturyan/Publication/3D_cube/cube_simulation/cube/"
time_steps=[]
polarization=[]
step=[]
name2="EpEp"
name1="EpEv"

for file in os.listdir('{}'.format(path_to_data)):
    if file.endswith(".txt") and name1 in file:
        with open (path_to_data+file, "r") as f:
            a=f.readlines()
            time_steps.append(float(a[4].split(" ")[-1]))
        if int(file.split("_")[1].split(".")[0]) not in step:
            step.append(int(file.split("_")[1].split(".")[0]))

step=sorted(np.array(step))
time_steps=sorted(np.array(time_steps))
p_values=[]
t,p=np.loadtxt('{}/P_t.p01'.format(path_to_data), unpack=True)

for s in time_steps:
    p_values.append(round(p[np.where(t==s)][0],3))

cor_val1=[]
cor_val2=[]
for i,j in zip(step,p_values):
    cor_val1.append(cor_func(name1,i,j))
    cor_val2.append(cor_func(name2,i,j))

cor_val1=np.array(cor_val1)
cor_val2=np.array(cor_val2)

plt.plot(p_values,np.sqrt(cor_val1+2*cor_val2)/2e6)
plt.show()
plt.xlim(-0.8,0.8)
#plt.ylim(-0.5, 0.5)
plt.savefig("{}.jpg".format(name1))
"""