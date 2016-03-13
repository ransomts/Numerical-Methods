import Text.Printf

main :: IO ()
main = print "Main"

legendre n x
   | n == 0 = x*0+1.0
   | n == 1 = x
   | otherwise = ((2.0*n-1.0)*x*(legendre (n-1) x)-(n-1)*(legendre (n-2) x))/n

dlegendre n x
   | n == 0 = x * 0
   | n == 1 = x*0+1.0
   | otherwise = (n/(x**2-1.0))*(x*(legendre n x)-(legendre (n-1) x))
