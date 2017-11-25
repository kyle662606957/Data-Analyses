# -*- coding: utf-8 -*-
import csv
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np
with open( 'G:\SNCR\CSV_4_SNCR\CH4_New__ADD_ITL.csv','rb') as f:
    reader = csv.reader(f)
    temperatures=[]
    CH4s=[]
    NOs=[]
    for row in reader:
       # print(row)
        try:
            Temperature=float(row[1])
            CH4=float(row[0])
            NO=float(row[3])
            temperatures.append(Temperature)
            CH4s.append(CH4)
            NOs.append(NO)
        except:
            continue
    s=['s','^','*','p','x']
    lgdArry=['0ppm CH4','300ppm CH4','600ppm CH4','900ppm CH4','1200ppm CH4']
    DataPoint=[];
    jj=-1
    for j in [0,1,2,3,4]:
        jj=jj+1
        temperature= np.array( [temperatures[i] for i in range(len(CH4s)) if CH4s[i]==0.0003*j])
        NO_CH4_jppm = np.array([NOs[i]/0.0002 for i in range(len(CH4s)) if CH4s[i]==0.0003*j])
        f=interp1d(temperature[1:], NO_CH4_jppm[1:],kind='cubic')# the 2 minimum values can not be the same

        temperature_new=np.linspace(temperature[1],temperature[-1],num=90,endpoint=True)
        ltemp,=plt.plot(temperature,NO_CH4_jppm,s[jj],label=lgdArry[jj],markersize=7)
        DataPoint.append(ltemp)
        plt.plot(temperature_new,f(temperature_new),'--')
        plt.show()
       # plt.hold(True)
plt.xlabel('Temperature ($^\circ$C)',fontsize='large')
plt.ylabel('NO out/ NO in',fontsize='large')
plt.legend(handles=DataPoint,fontsize='large')
#plt.savefig('CH4.eps',format="eps")
