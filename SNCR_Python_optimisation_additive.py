# -*- coding: utf-8 -*-
import csv
import bandwidth as bdw
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np
with open( '\\SNCR\\CSV_4_SNCR\\additive_optimization.csv','rb') as f:
    reader = csv.reader(f)
    temperatures=[]
    pressures=[]
    velocitys=[]
    NH3s=[]
    NOs=[]
    for row in reader:
       # print(row)
        try:
            Temperature=float(row[6])
            pressure=float(row[5])
            velocity=float(row[4])
            NH3=float(row[7])
            NO=float(row[9])
            temperatures.append(Temperature)
            pressures.append(pressure)
            velocitys.append(velocity)
            NH3s.append(NH3)
            NOs.append(NO)
        except:
            continue
    s=['s','^','*','p','x','D']
    jj=-1
    pressure_set=sorted(list(set(pressures)))
    velocity_set=sorted(list(set(velocitys)))
    for pressureX in pressure_set:
        for velocityX in velocity_set:
        #jj=jj+1
            temperature_J= np.array( [temperatures[i] for i in range(len(pressures)) \
              if abs(pressures[i]-pressureX)/(pressureX)<10**-3  \
                 and abs(velocitys[i]-velocityX)/(velocityX)<10**-3] )# the data can not be the value exacte,the range is necessary
            #NO_factor_j = np.array([NOs[i]/(0.00028*j+0.0001) for i in range(len(factors)) if abs(factors[i]-0.00028*j-0.0001)/(0.00028*j+0.0001)<10**-3])
            NO_Temprt_cas= np.array( [NOs[i] for i in range(len(pressures)) \
              if abs(pressures[i]-pressureX)/(pressureX)<10**-3  \
                 and abs(velocitys[i]-velocityX)/(velocityX)<10**-3] )

            f=interp1d(temperature_J[1:], NO_Temprt_cas[1:],kind='cubic')# the 2 minimum values can not be the same
            temperature_new=np.linspace(temperature_J[1],temperature_J[-1],num=90,endpoint=True)

            index_Min_NO=np.argmin(NO_Temprt_cas)
            optimal_Temperature=temperature_J[index_Min_NO]
            optimal_NO=NO_Temprt_cas[index_Min_NO]
            width=bdw.bandwidth(temperature_J,NO_Temprt_cas)
            #print("%d,%d"%(optimal_Temperature,optimal_NO))
            ########################################write it down###################################
            add_info = [pressureX,velocityX,optimal_Temperature,optimal_NO,width]
            csvFile = open("\SNCR\CSV_4_SNCR\SNCR_NO_Optimal.csv", "a")
            writer = csv.writer(csvFile,lineterminator='\n')
            writer.writerow(add_info)
            csvFile.close()
            ###########################################################plot the image###############
    # '''
    #         plt.figure()
    #         plt.plot(temperature_J,NO_Temprt_cas,'*',temperature_new,f(temperature_new),'--')
    #         plt.show()
    #         # plt.hold(True)
    #         plt.xlabel('Temperature ($^\circ$C)')
    #         plt.ylabel('NO out/ NO in')
    #         plt.legend(["pressure="+str(pressureX)+",velocity"+str(velocityX)])
    # '''
