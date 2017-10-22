import math
from math import pi as PI

def butterworth(n):
    g = [1.0]
    for i in range(1,n+1):
        g.append(round(2*math.sin((2*i-1)*math.pi/2/n),6))
    g.append(1.0)
    return g

def chebyshey(n, ripple):
    ep = math.sqrt(math.pow(10,0.1*ripple)-1)
    y = math.sinh(math.asinh(1/ep)/n)
    g = [1.0]
    temp = 2/y*math.sin(math.pi/2/n)
    g.append(round(temp,4))

    for i in range(1,n):
        temp = 4*math.sin((2*i-1)*math.pi/2/n)*math.sin((2*i+1)*math.pi/2/n)/(math.pow(y,2)+math.pow(math.sin(i*math.pi/n),2))/temp
        g.append(round(temp,4))

    if n % 2 == 0:    
        g.append(round(math.pow(ep+math.sqrt(1+ep*ep),2),4))
    else:
        g.append(1.0)
    return g

