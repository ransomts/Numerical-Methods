import math

def RK4(f):
    return lambda t, y, dt: (
            lambda dy1: (
            lambda dy2: (
            lambda dy3: (
            lambda dy4: (dy1 + 2*dy2 + 2*dy3 + dy4)/6
            )( dt * f( t + dt  , y + dy3   ) )
	    )( dt * f( t + dt/2, y + dy2/2 ) )
	    )( dt * f( t + dt/2, y + dy1/2 ) )
	    )( dt * f( t       , y         ) )
 
dy = RK4(lambda t, y: (2 - t) * y)
 
t, y, dt = 2., 1., .1
while t <= 10:
    if abs(round(t) - t) < 1e-5:
      	print("y(%2.1f)\t= %4.9f " % ( t, y))
    t, y = t + dt, y + dy( t, y, dt )

print("\n")

# I'm going to use the same coding style, and
#     just redefine the variables
dy = RK4(lambda t, y: 100 * (math.sin(t) - y))
t, y, dt = 0., 0., .015
oldY = y
while t <= 3.:
    # if abs(round(t) - t) < 1e-10:
    # This conditional was causing some
    #    problems with my output, it helps
    #    up top but here it cuts out most of the
    #    output I want, I'm taking it out because
    #    the point of the problem isn't the formatting
    print("y(%2.1f)\t= %4.9f " % ( t, y))
    t, y = t + dt, y + dy( t, y, dt )

print();
t, y, dt = 0., 0., .02
oldY = y
while t <= 3.:
    print("y(%2.1f)\t= %4.9f " % ( t, y))
    t, y = t + dt, y + dy( t, y, dt )

print();
t, y, dt = 0., 0., .025
oldY = y
while t <= 3.:
    print("y(%2.1f)\t= %4.9f " % ( t, y))
    t, y = t + dt, y + dy( t, y, dt )

print();
t, y, dt = 0., 0., .03
oldY = y
while t <= 3.:
    print("y(%2.1f)\t= %4.9f " % ( t, y))
    t, y = t + dt, y + dy( t, y, dt )
