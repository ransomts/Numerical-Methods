import Text.Printf

leftsum :: (Float -> Float) -> Float -> Float -> Float -> Float
leftsum f a b n =
  let h = (b-a)/n
  in h * sum (map f (map (\i -> a + i*h) [0..n-1]))


rightsum :: (Float -> Float) -> Float -> Float -> Float -> Float
rightsum f a b n =
  let h = (b-a)/n
  in h * sum (map f (map (\i -> a + i*h) [1..n]))

trapezoid_sum :: (Float -> Float) -> Float -> Float -> Float -> Float
trapezoid_sum f a b n =
  ((rightsum f a b n) + (leftsum f a b n)) / 2

foo :: Float -> Float
foo x = x**2

-- Really bad approximation of an integral
main :: IO ()
main = do
  printf "%.5f\n"  (leftsum foo 0 10 500)
  print(rightsum foo 0 10 500)
  print(trapezoid_sum foo 0 10 500)
