import numpy as np
import pandas as pd
df=pd.read_csv('G:\\SNCR\\CSV_4_SNCR\\additive_detail.csv',header=0).drop_duplicates()
add2=df[abs(df["Reactant Fraction for H2 C1 Inlet1 PFR (C1)_(mole_fraction)"]-9*(df["Reactant Fraction for CO2 C1 Inlet1 PFR (C1)_(mole_fraction)"]-0.15))<10e-7]
add1=df[abs(df["Reactant Fraction for H2 C1 Inlet1 PFR (C1)_(mole_fraction)"]-9*(df["Reactant Fraction for CO2 C1 Inlet1 PFR (C1)_(mole_fraction)"]-0.15))>10e-7]
df.count()
add1.count()
add2.count()
add2.head()
add2_0=add2[add2['Reactant Fraction for H2 C1 Inlet1 PFR (C1)_(mole_fraction)']==0]
add2_300=add2[add2['Reactant Fraction for H2 C1 Inlet1 PFR (C1)_(mole_fraction)']==8.10e-5]
add2_900=add2[abs(add2['Reactant Fraction for H2 C1 Inlet1 PFR (C1)_(mole_fraction)']-2.43e-4)<10e-7]

#add1_0=add1[add1['Reactant Fraction for H2 C1 Inlet1 PFR (C1)_(mole_fraction)']==0]
add1_300=add1[abs(add1['Reactant Fraction for H2 C1 Inlet1 PFR (C1)_(mole_fraction)']-0.000102)<10e-7]
add1_900=add1[abs(add1['Reactant Fraction for H2 C1 Inlet1 PFR (C1)_(mole_fraction)']-0.000306)<10e-7]
Exprmt_1_300=pd.read_csv('G:\SNCR\Compare_Delong_Simulation\\1_300.csv',header=0)
Exprmt_1_900=pd.read_csv('G:\SNCR\Compare_Delong_Simulation\\1_900.csv',header=0)
Exprmt_2_300=pd.read_csv('G:\SNCR\Compare_Delong_Simulation\\2_300.csv',header=0)
Exprmt_2_900=pd.read_csv('G:\SNCR\Compare_Delong_Simulation\\2_900.csv',header=0)
Exprmt_1_300['x']
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
def draw_image(indicator):
    #This is to analysis the data of 0ppm
    f=interp1d(add2_0['Temperature C1 PFR PFR (C1)_(C)'],100*add2_0[indicator]/0.0002,kind='cubic')
    temperature_new=np.linspace(555,1250,num=90,endpoint=True)
    plt.plot(temperature_new,f(temperature_new),'-')

    #For additive #1 NO
    #This is to analysis the data of 300ppm
    f=interp1d(add1_300['Temperature C1 PFR PFR (C1)_(C)'],100*add1_300[indicator]/0.0002,kind='cubic')
    temperature_new=np.linspace(555,1250,num=90,endpoint=True)
    plt.plot(Exprmt_1_300['x'],Exprmt_1_300['y'],'^',temperature_new,f(temperature_new),'--')
    #This is to analysis the data of 900ppm
    f=interp1d(add1_900['Temperature C1 PFR PFR (C1)_(C)'],100*add1_900[indicator]/0.0002,kind='cubic')
    temperature_new=np.linspace(555,1250,num=90,endpoint=True)
    plt.plot(Exprmt_1_900['x'],Exprmt_1_900['y'],'v',temperature_new,f(temperature_new),'--')

    #For additive #2  NO
    #This is to analysis the data of 300ppm
    f=interp1d(add2_300['Temperature C1 PFR PFR (C1)_(C)'],100*add2_300[indicator]/0.0002,kind='cubic')
    temperature_new=np.linspace(555,1250,num=90,endpoint=True)
    plt.plot(Exprmt_2_300['x'],Exprmt_2_300['y'],'s',temperature_new,f(temperature_new),'-.')
    #This is to analysis the data of 900ppm
    f=interp1d(add2_900['Temperature C1 PFR PFR (C1)_(C)'],100*add2_900[indicator]/0.0002,kind='cubic')
    temperature_new=np.linspace(555,1250,num=90,endpoint=True)
    plt.plot(Exprmt_2_900['x'],Exprmt_2_900['y'],'D',temperature_new,f(temperature_new),'-.')

    plt.xlabel('Temperature ($^\circ$C)',fontsize='large')
    plt.ylabel('NO(out)/NO(in)(%)',fontsize='large')
    plt.legend(['0ppm additive','300ppm additive#1 Experiment','300ppm additive#1 Simulation','900ppm additive#1 Experiment','900ppm additive#1 Simulation','300ppm additive#2 Experiment','300ppm additive#2 Simulation','900ppm additive#2 Experiment','900ppm additive#2 Simulation'])
    plt.title('Effect on NO with different concentrations of syngas',fontsize='large')
    plt.show()
draw_image(indicator='Mole fraction NO end point')
