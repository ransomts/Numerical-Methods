import math

# t0: initial independent variable
# x0: initial dependent variable
# tn: target value for the independent variable
# n: number of steps to take from t0 to tn
# f: right hand side function
'''
def abmpc(t0, x0, tn, n, f):
    h = (tn - t0)/ float(nsteps)
    t = t0
    x = x0
    
    for i in range(1, 3):
        k1 = f(i, t[i], x[i])
        k2 = f(i, t[i]+h/2.0, x[i]+ h*k1/2.0)
        k3 = f(i, t[i] + h/2.0, x[i] + h*k2/2.0)
        k4 = f(i, t[i] + h, x[i] + h*k3)
        
        x[i+1] = x[i] + h*(k1 + 2*(k2 + k3) + k4) / 6.0
        t[i+1] = t0 + i*h
        
    for i in range(1, 4):
        t[i+1] = t0 + i*h
        xpred = x[i] + h*(55.0*f(i,t[i],x[i]) - 59.0*f(i,t[i-1],x[i-1]) + 37.0*f(i,t[i-2],x[i-2]) - 9.0*f(i,t[i-3],x[i-3])) / 24.0
        x[i+1] = x[i] + h*(9.0*f(i,t[i+1],xpred) + 19.0*f(i,t[i],x[i]) - 5.0*f(i,t[i-1],x[i-1]) + f(i,t[i-2],x[i-2])) / 24.0

def f(i, t, x):
    if i == 0:
        return x * t
'''
