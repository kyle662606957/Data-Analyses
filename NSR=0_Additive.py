import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
df=pd.read_csv('G:\SNCR\CSV_4_SNCR\SNCR_NSR=0_T100.csv',header=0).drop_duplicates()
df.count()
add2=df[abs(df["Reactant Fraction for H2 C1 Inlet1 PFR (C1)_(mole_fraction)"]-9.0*(df["Reactant Fraction for CO2 C1 Inlet1 PFR (C1)_(mole_fraction)"]-0.15))<10e-6]
add2.count()
add1=df[abs(df["Reactant Fraction for H2 C1 Inlet1 PFR (C1)_(mole_fraction)"]-34.0/31.0*(df["Reactant Fraction for CO2 C1 Inlet1 PFR (C1)_(mole_fraction)"]-0.15))<10e-7]
#here we can not write 34/31, the python will take this as 1
#add1[add1["Reactant Fraction for H2 C1 Inlet1 PFR (C1)_(mole_fraction)"]==0].count()
add1.count()
h2_add1=np.linspace(0.000102,0.002754,num=14).tolist()
h2_add1.insert(0,0)# the first time I used h2_add1=h2_add1.inset, but it doesn t work, the result is not in the return value of insert
h2_add1=np.asarray(h2_add1[1:14:2])

h2_add2=np.linspace(0.27*3e-4,0.27*8.1e-3,num=14).tolist()
h2_add2.insert(0,0)# the first time I used h2_add1=h2_add1.inset, but it doesn t work, the result is not in the return value of insert
#h2_add2=np.asarray(h2_add2[1:14:3])
h2_add2=np.asarray([0,0.000081,0.000243,0.000405,0.000567,0.000729,0.000891,0.001053,0.001215,0.001377,0.001539,0.001701,0.001863, \
                    0.002025,0.002187][1:14:2])
h2_percentage=[0.34,0.27]


symbol=['s','^','o','*','v','d','1']
k=0
for i in [0,1]:
    addx=[add1,add2][i]
    h2_addx=[h2_add1,h2_add2][i]
    addx['Mole_Fraction_NOx']=addx['Mole fraction NO2 end point']+addx['Mole fraction NO end point']+addx['Mole fraction N2O end point']
    for indicator in ['Mole fraction NO end point','Mole fraction NO2 end point','Mole fraction N2O end point','Mole_Fraction_NOx']:
        plt.figure()
        plt.xlabel('Temperature ($^\circ$C)')
        plt.ylabel(indicator)
        lgd=[]
        for h2 in h2_addx:
            k=k+1
            dataSet=addx[abs(addx['Reactant Fraction for H2 C1 Inlet1 PFR (C1)_(mole_fraction)']-h2)<10e-6]
            f=interp1d(dataSet['Temperature C1 PFR PFR (C1)_(C)'],dataSet[indicator],kind='slinear')
            temperature_new=np.linspace(100,1240,num=90,endpoint=True)
            plt.plot(dataSet['Temperature C1 PFR PFR (C1)_(C)'],dataSet[indicator],symbol[k%7],temperature_new,f(temperature_new),'--',markersize=4)
            lgd.append('Addtive#'+str(i+1)+'='+str(h2/h2_percentage[i]))
            lgd.append('')
        plt.legend(lgd,fontsize='x-small')
        plt.show()
df2=pd.read_csv('G:\SNCR\CSV_4_SNCR\NSR_New__ADD_ITL.csv',header=0)
df2.head()
df2['Mole Fraction NOx']=df2['Mole fraction NO2 end point']+df2['Mole fraction NO end point']+df2['Mole fraction N2O end point']

symbol=['s','^','o','*','v','d','1']
l=0



for indicator in ['Mole fraction NO end point','Mole fraction NO2 end point','Mole fraction N2O end point','Mole Fraction NOx']:
    plt.figure()
    plt.xlabel('Temperature ($^\circ$C)')
    plt.ylabel(indicator)
    lgd=[]
    for j in range(5):
        l+=1
        dataSet=df2[abs(df2['Reactant Fraction for NH3 C1 Inlet1 PFR (C1)_(mole_fraction)']-0.00012*j)<10e-7].drop_duplicates()
        f=interp1d(dataSet['Temperature C1 PFR PFR (C1)_(C)'],dataSet[indicator],kind='cubic')
        temperature_new=np.linspace(550,1250,num=90,endpoint=True)
        plt.plot(dataSet['Temperature C1 PFR PFR (C1)_(C)'],dataSet[indicator],symbol[l%6],temperature_new,f(temperature_new),'--',)

        lgd.append('NSR='+str(j*0.00012/0.0002)+":"+"NH3="+str(j*0.00012))
        lgd.append(' ')
    plt.legend(lgd,fontsize='x-small')
    plt.show()

