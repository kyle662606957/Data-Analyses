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
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
def draw_image(indicator):
    plt.figure()
    #This is to analysis the data of 0ppm
    f=interp1d(add2_0['Temperature C1 PFR PFR (C1)_(C)'],add2_0[indicator],kind='cubic')
    temperature_new=np.linspace(555,1250,num=90,endpoint=True)
    plt.plot(add2_0['Temperature C1 PFR PFR (C1)_(C)'],add2_0[indicator],'*',temperature_new,f(temperature_new),'--')

    #For additive #1 NO
    #This is to analysis the data of 300ppm
    f=interp1d(add1_300['Temperature C1 PFR PFR (C1)_(C)'],add1_300[indicator],kind='cubic')
    temperature_new=np.linspace(555,1250,num=90,endpoint=True)
    plt.plot(add1_300['Temperature C1 PFR PFR (C1)_(C)'],add1_300[indicator],'^',temperature_new,f(temperature_new),'--')
    #This is to analysis the data of 900ppm
    f=interp1d(add1_900['Temperature C1 PFR PFR (C1)_(C)'],add1_900[indicator],kind='cubic')
    temperature_new=np.linspace(555,1250,num=90,endpoint=True)
    plt.plot(add1_900['Temperature C1 PFR PFR (C1)_(C)'],add1_900[indicator],'v',temperature_new,f(temperature_new),'--')

    #For additive #2  NO
    #This is to analysis the data of 300ppm
    f=interp1d(add2_300['Temperature C1 PFR PFR (C1)_(C)'],add2_300[indicator],kind='cubic')
    temperature_new=np.linspace(555,1250,num=90,endpoint=True)
    plt.plot(add2_300['Temperature C1 PFR PFR (C1)_(C)'],add2_300[indicator],'s',temperature_new,f(temperature_new),'--')
    #This is to analysis the data of 900ppm
    f=interp1d(add2_900['Temperature C1 PFR PFR (C1)_(C)'],add2_900[indicator],kind='cubic')
    temperature_new=np.linspace(555,1250,num=90,endpoint=True)
    plt.plot(add2_900['Temperature C1 PFR PFR (C1)_(C)'],add2_900[indicator],'D',temperature_new,f(temperature_new),'--')

    plt.xlabel('Temperature ($^\circ$C)',fontsize='large')
    plt.ylabel(indicator,fontsize='large')
    #plt.show()
    plt.legend(['0ppm additive','','300ppm additive#1','','900ppm addtive #1','','300ppm additive#2','','900ppm additive#2',''],fontsize='large')

draw_image(indicator='Mole fraction NO end point')
draw_image(indicator='Mole fraction NO2 end point')
draw_image(indicator='Mole fraction N2O end point')
draw_image(indicator='Mole fraction NH3 end point')
