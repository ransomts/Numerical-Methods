import math
'''
Implementation of the Trapazoid method and Simpnon's method of numerical integration.
'''
def trapezoid(f, a, b, n):
# f: continuous funciton to estimate the signed area for
# a and b: the limets of integration (with a<b)
# n: the number of subintervals desired
  h = (b - a) / n
  # summation form of an integral with a divide by zero check
  ival = h * sum( (f(a+i*h) + f(a+i*h+h))/2 for i in range(n))
  print("Trapazoid: ", ival)

def simpson(f, a, b, n):
   if n % 2:
      print("n must be even")
      return
   h = (b - a) / n
   s = f(a) + f(b)

   for i in range(1, n, 2):
      s += 4 * f(a + i * h)
   for i in range(2, n - 1, 2):
      s += 2 * f(a + i * h)

   return s * h / 3

