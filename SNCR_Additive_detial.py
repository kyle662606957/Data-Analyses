import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
df=pd.read_csv('G:\\SNCR\\CSV_4_SNCR\\SNCR_ADDITIVE_Detail.csv',header=0).drop_duplicates()
df.count()
add2=df[abs(df["Reactant Fraction for H2 C1 Inlet1 PFR (C1)_(mole_fraction)"]-9*(df["Reactant Fraction for CO2 C1 Inlet1 PFR (C1)_(mole_fraction)"]-0.15))<10e-7]
add2[add2["Reactant Fraction for H2 C1 Inlet1 PFR (C1)_(mole_fraction)"]==0].count()
# To check if the data has the right amount
add1=df[abs(df["Reactant Fraction for H2 C1 Inlet1 PFR (C1)_(mole_fraction)"]-34.0/31.0*(df["Reactant Fraction for CO2 C1 Inlet1 PFR (C1)_(mole_fraction)"]-0.15))<10e-7]
#here we can not write 34/31, the python will take this as 1
#add1[add1["Reactant Fraction for H2 C1 Inlet1 PFR (C1)_(mole_fraction)"]==0].count()
add1.count()
#This is to analysys the parameter residence time
symbol=['s','^','o']
symbol2=[':','--','-']
i=-1
j=0
k=0
l=0
fraction_H2=[0.34,0.27]
Parameter_Study=['ppm NSR=','ppm  ResidTime=']
Parameter_Study2=[' NSR ',' residence time ']
Parameter_Value=['str(NSR)','str(45.0/velocity)']
Parameter_Value2=['','s']
for addx in [add1,add2]:
    i+=1
    for indicator in ['Mole fraction NO end point','Mole fraction NO2 end point','Mole fraction N2O end point','Mole fraction NH3 end point']:

        for (velocity,NSR) in zip([75.0,50.0,25.0,75,75,75],[1.5,1.5,1.5,1.5,1.8,2]):
            j=j+1
            if j%3==1:
                #plt.figure()
                lgd=[]
                k+=1
                plt.xlabel('Temperature ($^\circ$C)',fontsize='large')
                plt.ylabel(indicator,fontsize='large')
                plt.title('The Influence of'+Parameter_Study2[k%2] +'with'+' Additive#'+str(i+1),fontsize='large')
            for concentration in [0e-6,300e-6,900e-6]:
                l+=1
                dataSet=addx[(abs(addx['Reactant Fraction for H2 C1 Inlet1 PFR (C1)_(mole_fraction)']-concentration*fraction_H2[i])<10e-7) & \
                             (abs(addx['Axial Velocity C1 Inlet1 PFR (C1)_(cm/sec)']-velocity)<10e-7) &  \
                             (abs(addx['Reactant Fraction for NH3 C1 Inlet1 PFR (C1)_(mole_fraction)']-0.0002*NSR)<10e-7) ].sort_values(by='Temperature C1 PFR PFR (C1)_(C)')
                f=interp1d(dataSet['Temperature C1 PFR PFR (C1)_(C)'],dataSet[indicator],kind='cubic')
                temperature_new=np.linspace(555,1250,num=90,endpoint=True)
                plt.plot(dataSet['Temperature C1 PFR PFR (C1)_(C)'],dataSet[indicator],symbol[j%3],temperature_new,f(temperature_new),symbol2[l%3])
                #lgd.append('')
                lgd.append('additive='+str(concentration*10**6)+Parameter_Study[k%2]+eval(Parameter_Value[k%2])+Parameter_Value2[k%2])
                lgd.append('')
            if j%3==0:
                #plt.legend(lgd,fontsize='xx-small')
                #plt.show()
                plt.savefig('G:\SNCR\Fig\PHOTO1\\'+indicator+'addx'+str(i)+Parameter_Study2[k%2]+'result.png',bbox_inches='tight')
                plt.close()
