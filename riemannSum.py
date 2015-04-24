import math

def leftsum(f, a, b, n):
# f: continuous funciton to estimate the signed area for
# a and b: the limets of integration (with a<b)
# n: the number of subintervals desired
  h = (b - a) / n
  print("Left Sum: ", h * sum( f(a+i*h) for i in range(n)) )
               #      |     \                    |
               #  Step size  summation       of all my rectangles
               #  (factored out)
def trapezoid(f, a, b, n):
# f: continuous funciton to estimate the signed area for
# a and b: the limets of integration (with a<b)
# n: the number of subintervals desired
  h = (b - a) / n
  # summation form of an integral with a divide by zero check
  ival = h * sum( (f(a+i*h) + f(a+i*h+h))/2 for i in range(n))
  print("Trapazoid: ", ival)

# For 10^-12 error max, trap needs 2473082 steps
#                       
print("2a")
leftsum(lambda x: math.exp(math.sin(x)), 0, 3, 100)
trapezoid(lambda x: math.exp(math.sin(x)), 0, 3, 100)

# For 10^-12 error max, trap needs 9724300 steps
#
print("2b")
leftsum(lambda x: x**2 * math.log(x) + 100, 1, 1000, 100)
trapezoid(lambda x: x**2 * math.log(x) + 100, 1, 1000, 100)

# For 10^-12 error max, trap needs 14907120 steps
#
print("2c")
leftsum(lambda x: math.sin(x) / x, -10, 10, 101)
trapezoid(lambda x: math.sin(x) / x, -10, 10, 101)
# In assignment 4, the program computed the ln(b) 



