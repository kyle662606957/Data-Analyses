# -*- coding: utf-8 -*-
import csv
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np
with open( 'G:\SNCR\CSV_4_SNCR\CO_New__ADD_ITL.csv','rb') as f:
    reader = csv.reader(f)
    temperatures=[]
    COs=[]
    NOs=[]
    for row in reader:
       # print(row)
        try:
            Temperature=float(row[0])
            CO=float(row[1])
            NO=float(row[3])+float(row[5])
            temperatures.append(Temperature)
            COs.append(CO)
            NOs.append(NO)
        except:
            continue
    s=['s','^','*','p','x']
    lgdArry=['0ppm CO','300ppm CO','600ppm CO','900ppm CO','1200ppm CO']
    jj=-1
    DataPoint=[]
    for j in [0,1,2,3,4]:
        jj=jj+1
        temperature= np.array( [temperatures[i] for i in range(len(COs)) if COs[i]==0.0003*j])
        NO_CO_0ppm = np.array([NOs[i]/0.0002 for i in range(len(COs)) if COs[i]==0.0003*j])
        f=interp1d(temperature[1:], NO_CO_0ppm[1:],kind='cubic')# the 2 minimum values can not be the same

        temperature_new=np.linspace(temperature[1],temperature[-1],num=90,endpoint=True)
        ltemp,=plt.plot(temperature,NO_CO_0ppm,s[jj],label=lgdArry[jj],markersize=7)
        DataPoint.append(ltemp)
        plt.plot(temperature_new,f(temperature_new),'--')
        plt.show()
       # plt.hold(True)
plt.xlabel('Temperature ($^\circ$C)',fontsize='large')
plt.ylabel('NO out/ NO in',fontsize='large')
plt.legend(handles=DataPoint,fontsize='large')
