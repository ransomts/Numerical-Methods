def rk4(n, t0, x0, tn, nsteps, f):
    # n - number of equations
    # t0 - initial independent variable
    # x0 - initial dependent variable values(array)
    # tn - target value for the independent variable
    # tn - number of steps to take from t0 to tn
    # f - right hand side functions (array - OR use one function with if statements
    h = (tn - t0)/ float(nsteps)
    t = t0
    x = x0
    
    k1 = [float(0) for i in range(n)]
    k2 = [float(0) for i in range(n)]
    k3 = [float(0) for i in range(n)]
    k4 = [float(0) for i in range(n)]
    temp = [float(0) for i in range(n)]

    for j in range(1, nsteps):
        for i in range(n):
            k1[i] = f(i, t, x)
            
            for z in range(n): temp[z] = x[z] + (h*(k1[z]/2.0))
            k2[i] = f(i, t+(h/2.0), temp)
            
            for z in range(n): temp[z] = x[z] + (h*(k2[z]/2.0))
            k3[i] = f(i, t+(h/2.0), temp)
            
            for z in range(n): temp[z] = x[z] + (h*k3[z])
            k4[i] = f(i, t+h, temp)
            
            x[i]= x[i] + h*(k1[i] + 2*(k2[i] + k3[i]) + k4[i]) / 6.0
            
        t = t0 + j*h
        print t, x
        
def f(i, t, x):
    if i==0:
        return 1.0
    elif i==1:
        return -x[2]+math.cos(x[0])
    else:
        return x[1]+math.sin(x[0])
