import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
df=pd.read_csv('G:\\SNCR\CSV_4_SNCR\\NSR=06_1_12_Additive.csv',header=0).drop_duplicates()
df['Mole Fraction NOx']=df['Mole fraction NO2 end point']+df['Mole fraction NO end point']+df['Mole fraction N2O end point']
df.count()
add2=df[abs(df["Reactant Fraction for H2 C1 Inlet1 PFR (C1)_(mole_fraction)"]-9.0*(df["Reactant Fraction for CO2 C1 Inlet1 PFR (C1)_(mole_fraction)"]-0.15))<10e-7]
add2.count()
add1=df[abs(df["Reactant Fraction for H2 C1 Inlet1 PFR (C1)_(mole_fraction)"]-34.0/31.0*(df["Reactant Fraction for CO2 C1 Inlet1 PFR (C1)_(mole_fraction)"]-0.15))<10e-7]
#here we can not write 34/31, the python will take this as 1
#add1[add1["Reactant Fraction for H2 C1 Inlet1 PFR (C1)_(mole_fraction)"]==0].count()
add2.head(7)
symbol=['1','^','x','*','v','s','+','o']
for i in [1,2]:
    addx=[add1,add2][i-1]
    H2_Initial=[0.000408,0.000324][i-1]
    for NSR in [0.6,1,1.2]:
        for indicator in ['Mole fraction NO end point','Mole fraction NO2 end point','Mole fraction N2O end point','Mole fraction NH3 end point','Mole Fraction NOx']:
            #plt.figure()
            plt.xlabel('Temperature ($^\circ$C)')
            plt.ylabel(indicator)
            plt.title('NSR='+str(NSR))
            lgd=[]
            for j in range(8):
                dataSet=addx[(addx['Reactant Fraction for NH3 C1 Inlet1 PFR (C1)_(mole_fraction)']==NSR*0.0002) & (abs(addx['Reactant Fraction for H2 C1 Inlet1 PFR (C1)_(mole_fraction)']-H2_Initial*j)<10e-7)]
                f=interp1d(dataSet['Temperature C1 PFR PFR (C1)_(C)'],dataSet[indicator],kind='cubic')
                temperature_new=np.linspace(100,1240,num=90,endpoint=True)
                plt.plot(dataSet['Temperature C1 PFR PFR (C1)_(C)'],dataSet[indicator],symbol[j],temperature_new,f(temperature_new),'--',markersize=4)
                lgd.append('Addtive#'+str(i)+'='+str(0.0012*j))
                lgd.append('')
            plt.legend(lgd,fontsize='x-small')
            plt.savefig('G:\SNCR\Fig\PHOTO1\\'+indicator+'test.png')
            plt.close()
            #plt.show()
