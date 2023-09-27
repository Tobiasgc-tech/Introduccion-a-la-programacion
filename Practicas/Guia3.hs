--Ejercio1 a
f:: Int ->Int
f x | x == 1 = 8
    | x == 4 = 131
    | x == 16 = 16

--Ejercio1 b
g:: Int -> Int
g x | x == 8 = 16
    | x == 16 = 4
    | x == 131 = 1

--Ejercio1 c   
h:: Int -> Int
h x = f (g x)

k:: Int -> Int
k x = g (f x)

--Ejercio2 a
absoluto :: Int -> Int
absoluto x | x >= 0 = x
           | x < 0 = -x

--Ejercio2 b
maximoabsoluto :: Int -> Int -> Int
maximoabsoluto x y | absoluto x >= absoluto y = absoluto x
                   | absoluto x < absoluto y = absoluto y

--Ejercio2 c
maximo3 :: Int -> Int -> Int -> Int
maximo3 x y z | x >= y && x >= z = x
              | y >= x && y >= z = y
              | otherwise = z

--Ejercio2 d
algunoEs0 :: Float -> Float ->  Bool
algunoEs0 0 _ = True
algunoEs0 _ 0 = True
algunoEs0 _ _ = False

algunoEs0bis :: Float -> Float -> Bool
algunoEs0bis x y = x==0 || y==0

--Ejercio2
ambosSon0 :: Int -> Int -> Bool
ambosSon0 0 0 = True
ambosSon0 _ _ = False

--Ejercio2 f
mismoIntervalo :: Float -> Float -> Bool
mismoIntervalo x y | x <= 3 && y <= 3 = True
                   | x > 3 && x <= 7 && y > 3 && y <= 7 = True
                   |  x > 7 && y > 7 = True
                   | otherwise = False

--Ejercio2 g
sumaDistino :: Int -> Int -> Int -> Int
sumaDistino x y z | x /= y && x /= z && y /= z = x + y + z
                  | x == y &&  x == z = 0
                  | y == z = x
                  | x == z = y
                  | otherwise = z

--Ejercio2 h
esMultiplode :: Int -> Int -> Bool
esMultiplode x y | mod x y == 0 = True
                 | otherwise = False

--Ejercio2 i
digitoUnidades :: Int -> Int
digitoUnidades x | x < 0 = mod (-1*x) 10
                 | otherwise =mod x 10

--Ejercio2 j
digitoDecenas :: Int -> Int
digitoDecenas x | x < 0 = digitoUnidades (div (-1*x) 10)
                | otherwise = digitoUnidades (div x 10)

--Ejercio3
estanRelacionados :: Int -> Int -> Bool
estanRelacionados x y | esMultiplode x y = True
                      | otherwise = False

--Ejercio4 a
prodInt :: (Float,Float) -> (Float,Float) -> Float
prodInt (a1, a2) (b1, b2) = a1*b1 + a2*b2

--Ejercio4 b
todoMenor1 :: (Float,Float) -> (Float, Float) -> Bool
todoMenor1 v w | fst v < fst w && snd v < snd w = True
              | otherwise = False

todoMenor2 :: (Float,Float) -> (Float, Float) -> Bool
todoMenor2 v w = fst v < fst w && snd v < snd w

todoMenor3 :: (Float,Float) -> (Float, Float) -> Bool
todoMenor3 (v1, v2) (w1, w2) =  v1 < w1 && v2 < w2

--Ejercio4 c
distanciaPuntos :: (Float, Float) -> (Float, Float) -> Float
distanciaPuntos (x1, x2) (y1, y2) = sqrt ((x2-x1)**2 + (y2-y1)**2)

--Ejercio4 d
sumaTerna :: (Int, Int, Int) -> Int
sumaTerna (a,b,c) = a+b+c

--Ejercio4 e
sumarSoloMultiplos1 :: (Int, Int, Int) -> Int -> Int
sumarSoloMultiplos1 (a,b,c) x| mod a x == 0 && mod b x == 0 && mod c x == 0 = a+b+c
                             | mod a x == 0 && mod b x == 0 = a+b
                             | mod a x == 0 && mod c x == 0 = a+c
                             | mod a x == 0 = a
                             | mod b x == 0 && mod c x == 0 = b+c
                             | mod b x == 0 = b
                             | mod c x == 0 = c
                             | otherwise = 0

sumarSoloMultiplos2 :: (Int, Int, Int) -> Int -> Int
sumarSoloMultiplos2 (a,b,c) n = esMultiplo a n + esMultiplo b n + esMultiplo c n
        where
            esMultiplo :: Int -> Int -> Int
            esMultiplo a x | mod a x == 0 = a
                           | otherwise    = 0

--Ejercio4 f
posPrimerPar :: (Int, Int, Int) -> Int
posPrimerPar (a,b,c) | mod a 2 == 0 = 0
                     | mod b 2 == 0 = 1
                     | mod c 2 == 0 = 2
                     | otherwise = 4

--Ejercio4 g
crearPar :: a -> b -> (a, b)
crearPar a b = (a, b)

--Ejercio4 h
invertir :: (a, b) -> (b ,a)
invertir (a, b) = (b, a)

--Ejercio5 (suma + 2)
todosMenores :: (Integer, Integer, Integer) -> Bool
todosMenores (a,b,c) = f a > g a && f b > g b && f c > g c
    where
        f :: Integer -> Integer
        f n | n <= 7 = n ^ 2
            | n > 7 = 2*n-1

        g :: Integer -> Integer
        g n | mod n 2 == 0 = div n 2
            | otherwise =  3*n + 1

--Ejercio6
bisiesto :: Integer -> Bool
bisiesto x = not (mod x 4 /= 0 || mod x 100 == 0 && mod x 400 /= 0)

--Ejercio 7
distanciaManhatthan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhatthan (p0,p1,p2) (q0,q1,q2) = abs (p0-q0) + abs (p1-q1) + abs (p2-q2)

--Ejercio 8
comparar :: Integer -> Integer -> Integer
comparar a b | sumarUltimosDosDigitos a < sumarUltimosDosDigitos b = 1
             | sumarUltimosDosDigitos a > sumarUltimosDosDigitos b = -1
             | otherwise = 0
        where
            sumarUltimosDosDigitos :: Integer -> Integer
            sumarUltimosDosDigitos x = mod x 10 + mod (div x 10) 10