import numpy as np
import matplotlib.pyplot as plt


def f(x,y):
    return np.exp(-x**2-y**2)

def g(x,y):
    return np.exp(-(x-1)**2-(y-1)**2)

def h(x,y):
    return 2*(f(x,y)-g(x,y))

def find_seed(g,absinf,abssup,c=0,eps=2**(-26)):
    if (g(absinf)-c)*(g(abssup)-c)>0:
        return None
    else:
        deb=absinf
        fin=abssup
        m=(deb+fin)/2
        if g(absinf)>=g(abssup):
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


def simple_contour_initial(f,absinf,abssup,c=0,delta=0.01):
    x=list(np.linspace(absinf,abssup,(abssup-absinf)//delta+1))
    y=[]
    for valeur in x:
        def g(t):
            return f(valeur,t) # recherche du zéro de f à abscisse fixée
        y.append(find_seed(g,absinf,abssup))
    if None in y:
        return ([],[])
    else:
        return (x,y)

def simple_contour_gauche(f,absinf,abssup,c=0,delta=0.01):
    x=list(np.linspace(absinf,abssup,int((abssup-absinf)//delta+1)))
    y=[]
    for valeur in x:
        def g(t):
            return f(valeur,t) # recherche du zéro de f à abscisse fixée
        y.append(find_seed(g,absinf,abssup))
    if None in y:
        return ([],[])
    else:
        return (x,y)

def simple_contour_droite(f,absinf,abssup,c=0,delta=0.01):
    x=list(np.linspace(absinf,abssup,int((abssup-absinf)//delta+1)))
    y=[]
    for valeur in x:
        def g(t):
            return f(abssup-valeur,t) # recherche du zéro de f à abscisse fixée
        y.append(find_seed(g,absinf,abssup))
    if None in y:
        return ([],[])
    else:
        return (x,y)

def simple_contour_haut(f,ordinf,ordsup,c=0,delta=0.01):
    y=list(np.linspace(ordinf,ordsup,int((ordsup-ordinf)//delta+1)))
    x=[]
    for valeur in y:
        def g(t):
            return f(t,ordsup-valeur) # recherche du zéro de f à abscisse fixée
        y.append(find_seed(g,ordinf,ordsup))
    if None in y:
        return ([],[])
    else:
        return (x,y)

def simple_contour_bas(f,ordinf,ordsup,c=0,delta=0.01):
    y=list(np.linspace(ordinf,ordsup,int((ordsup-ordinf)//delta+1)))
    x=[]
    for valeur in y:
        def g(t):
            return f(t,valeur) # recherche du zéro de f à abscisse fixée
        y.append(find_seed(g,ordinf,ordsup))
    if None in y:
        return ([],[])
    else:
        return (x,y)

def contour(f,c=0.0,xc=[0.0,1.0],yc=[0.0,1.0],delta=0.01):
    xs=[]
    ys=[]
    for i in range(len(xc)):
        for j in range(len(yc)):
            a,b=simple_contour_gauche(f,xc[i],xc[i+1])
            xs.append(a)
            ys.append(b)
            a,b=simple_contour_droite(f,xc[i],xc[i+1])
            xs.append(a)
            ys.append(b)
            a,b=simple_contour_haut(f,yc[j],yc[j+1])
            xs.append(a)
            ys.append(b)
            a,b=simple_contour_bas(f,yc[j],yc[j+1])
            xs.append(a)
            ys.append(b)
    return xs,ys

print(contour(h))






