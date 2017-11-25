# -*- coding: utf-8 -*-
import csv
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np
with open( 'G:\SNCR\CSV_4_SNCR\NSR_New__ADD_ITL.csv','rb') as f:
    reader = csv.reader(f)
    temperatures=[]
    factors=[]
    NOs=[]
    for row in reader:
        #print(row)
        try:
            Temperature=float(row[0])
            factor=float(row[1])
            NO=float(row[3])
            temperatures.append(Temperature)
            factors.append(factor)
            NOs.append(NO)
        except:
            continue
    s=['s','^','*','p','x','D']
    jj=-1
    dataPoint=[]
    lgdArry=['NSR=0','NSR=0.6','NSR=1.2','NSR=1.8','NSR=2.4','NSR=3.0']
    for j in [0,1,2,3,4,5]:
        jj=jj+1
        temperature= np.array( [temperatures[i] for i in range(len(factors)) if abs(factors[i]-j*0.00012)<10**-5])# the data can not be the value exacte,the range is necessary
        NO_factor_j = np.array([NOs[i]/0.0002 for i in range(len(factors)) if abs(factors[i]-j*0.00012)<10**-5])
        f=interp1d(temperature[0:], NO_factor_j[0:],kind='cubic')# the 2 minimum values can not be the same

        temperature_new=np.linspace(temperature[0],temperature[-1],num=90,endpoint=True)
        ltmp,=plt.plot(temperature,NO_factor_j,s[jj],label=lgdArry[jj],markersize=6)
        dataPoint.append(ltmp)
        plt.plot(temperature_new,f(temperature_new),'--')
        plt.show()
       # plt.hold(True)
plt.xlabel('Temperature ($^\circ$C)',fontsize='large')
plt.ylabel('NO out/ NO in',fontsize='large')
plt.legend(handles=dataPoint,fontsize='large')
