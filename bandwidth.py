import numpy as np
f=list(np.linspace(0,4,100))
amplitude=list(abs((np.linspace(0,4,100)-100)))
def bandwidth(x,y):
    signal=np.array(y)
    indexMin=np.argmin(signal)
    minimumValue=signal[indexMin]
    distance_linge_milieux=np.array([abs(signalX-signal[0]+(signal[0]-minimumValue)/(2**0.5)) for signalX in signal ])
    #print signal[0],minimumValue,(signal[0]-minimumValue)/(2**0.5)
    index1=np.argmin(distance_linge_milieux[0:indexMin])
    #In the very beginning, I thought this index2 can give me the real index, but it just gave me the index relative in the arry[Indexmin:]
    index2=np.argmin(distance_linge_milieux[indexMin:])+indexMin
    return abs(x[index1]-x[index2])

if __name__ == "__main__":
    width=bandwidth(f,amplitude)

