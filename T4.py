import math

'''
This is an implementation of the Taylor's series metod of approximating
ordinary differenetial equations. Not quite as effective as the Runge Kutta
method.
'''

def T4():

# initial conditions x(0) = 1, step size of 1/100
   x = 1
   t = 0
   h = 0.01

   while t <= 1:
      print("t = %2.3f\tx = %9.9f" % (t, x))
      st = 1 + t # the successor of t
      xp    =    x / st
      xpp   =   xp / st - x / (st**2)
      xppp  =  xpp / st - 2*xp / (st**2) + 2*x / (st**3)
      xpppp = xppp / st - 3*xpp / (st**2) + 2*xp / (st**3) + 6*x / (st**4)

      x = x + h * (xp + h/2 * (xpp + h/3 * (xppp + h/4*xpppp)))
      
      t = t + h # this could cause some error

T4()
