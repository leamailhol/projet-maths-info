import numpy as np

def f(x,y):
    return np.exp(-x**2-y**2)

def g(x,y):
    return np.exp(-(x-1)**2-(y-1)**2)

def h(x,y):
    return 2*(f(x,y)-g(x,y))

def j(x):
    return h(0,x)

def find_seed(g,c=0,eps=2**(-26)):
    if (g(0)-c)*(g(1)-c)>0:
        return None
    else:
        deb=0
        fin=1
        m=(deb+fin)/2
        if g(0)>=g(1):
            dec=True
        else :
            dec=False
        while np.abs((g(m)-c))>eps:
            if g(m)>c:
                if dec:
                    deb=m
                else:
                    fin=m
            elif g(m)<c:
                if dec:
                    fin=m
                else:
                    deb=m
            m=(deb+fin)/2
        return m

print(find_seed(j))

