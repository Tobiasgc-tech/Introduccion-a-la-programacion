--PRACTICA N°4--
--Ejercio1
fibo :: Integer -> Integer
fibo n | n == 0 = 0
       | n == 1 = 1
       | otherwise = fibo (n-1) + fibo (n-2)

fiboPM :: Integer -> Integer
fiboPM 0 = 0
fiboPM 1 = 1
fiboPM n = fiboPM (n-1) + fiboPM (n-2)

--Ejercio2
parteEntera :: Float -> Integer
parteEntera x | x < 1 && x >= 0 = 0
              | x > -1 && x <= 0 = -1
              | x >= 1 = 1 + parteEntera ( x - 1 )
              | otherwise = (-1) + parteEntera ( x + 1 )

--Ejercio3
esDivisible :: Integer -> Integer -> Bool
esDivisible x y | x == y = True
                | x < y = False
                | x - y /= 0 = esDivisible (x-y) y

--Ejercio4
sumaImpares :: Integer -> Integer
sumaImpares 1 = 1
sumaImpares n = n^2

--Ejercio5
medioFact :: Integer -> Integer
medioFact 0 = 1
medioFact 1 = 1
medioFact 2 = 2
medioFact n = n * medioFact (n-2)

--Ejercio6
sumaDigitos :: Integer -> Integer
sumaDigitos x | x < 10 = x
              | otherwise = mod x 10 + sumaDigitos (div x 10)

--Ejercio7
todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | n < 10 = True
                      | otherwise = ultimoDijito n == ultimoDijito (sacarUltimo n) && todosDigitosIguales (sacarUltimo n )

ultimoDijito :: Integer -> Integer
ultimoDijito n = mod n 10

sacarUltimo :: Integer -> Integer
sacarUltimo n = div n 10

--Ejercio8
cantDigitos :: Integer -> Integer
cantDigitos n | n < 10 = 1
              | otherwise = 1 + cantDigitos (sacarUltimo n)

iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i | i == cantDigitos n = ultimoDijito n
                 | otherwise = iesimoDigito (sacarUltimo n) i

--Ejercio9
esCapicua :: Integer -> Bool
esCapicua n = n `div` reverseNumber n == 1

--Función para dar vuelta un número
reverseNumber :: Integer -> Integer
reverseNumber n = reverseHelper n 0

--Función auxiliar recursiva
reverseHelper :: Integer -> Integer -> Integer
reverseHelper 0 resultado = resultado
reverseHelper n resultado = reverseHelper (n `div` 10) (resultado * 10 + (n `mod` 10))

--Ejercio10
f1 :: Integer -> Integer
f1 0 = 1
f1 n = 2^n -1

--Ejercio11 a
eAprox :: Float -> Float
eAprox 0 = 1
eAprox x =  (1 / factorial x) + eAprox (x-1)

factorial :: Float -> Float
factorial x | x == 0 = 1
            | x == 1 = 1
            |otherwise = x * factorial (x-1)

--Ejercio12 --------AYUDAAA
raizDe2Aprox :: Integer -> Float
raizDe2Aprox 1 = 2
raizDe2Aprox n = (2 + 1 / raizDe2Aprox (n - 1)) - 1


--Ejercio13
funcion :: Int -> Int -> Int
funcion filas columnas = recorridoFilasHasta filas columnas

recorridoFilasHasta :: Int -> Int ->Int
recorridoFilasHasta 1 columnas = sumaFila 1 columnas
recorridoFilasHasta filas columnas = sumaFila filas columnas + recorridoFilasHasta (filas-1) columnas

sumaFila :: Int -> Int -> Int
sumaFila filas 1 = filas --fila
sumaFila filas columnas = filas ^ columnas + sumaFila filas (columnas-1)

--Ejercio14
sumaPotenciasM :: Integer -> Integer -> Integer -> Integer
sumaPotenciasM q n m | n < 1 = 0
                     | otherwise = q^(m+n) + sumaPotenciasM q (n-1) m

sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias q n m | m < 1 = 0
                    | otherwise = sumaPotenciasM q n m + sumaPotenciasM q n (m-1)

--Ejercio15
sumaRacionalesInt :: Float -> Float -> Float
sumaRacionalesInt _ 0 = 0
sumaRacionalesInt n q = (n / q) + sumaRacionalesInt n (q-1)

sumaRacionales :: Float -> Float -> Float
sumaRacionales 0 _ = 0
sumaRacionales n q = sumaRacionales (n-1) q + sumaRacionalesInt n q

--Ejercio16 a
menorDivisor :: Integer -> Integer
menorDivisor n = menorDivisorDesde n 2
 where
    menorDivisorDesde :: Integer -> Integer -> Integer
    menorDivisorDesde n desde | mod n desde == 0 = desde
                              | otherwise = menorDivisorDesde n (desde + 1)

--Ejercio16 b
esPrimo :: Integer -> Bool
esPrimo n = menorDivisor n == n

--Ejercio16 c ------AYUDAAAAA
--sonCoprimos :: Integer -> Integer -> Bool

--Ejercio16 d ------AYUDAAAAA
nEsimoPrimo :: Integer ->Integer
nEsimoPrimo 1 = 2
nEsimoPrimo n = 0

--Ejercio17
esFibonacci :: Integer ->Bool
esFibonacci n = n == fibo n+1


--Ejercio19
esSumaInicialDePrimos :: Integer -> Bool
esSumaInicialDePrimos suma = esSumaInicialDePrimosHasta suma 2

esSumaInicialDePrimosHasta :: Integer -> Integer -> Bool
esSumaInicialDePrimosHasta suma hasta | sumarPrimos suma == suma = True
                                      | sumarPrimos suma < suma = False
                                      | otherwise = esSumaInicialDePrimosHasta suma (hasta + 1)

sumarPrimos :: Integer -> Integer
sumarPrimos 2 = 2
sumarPrimos n | esPrimo n = n + sumarPrimos (n - 1)
              | otherwise = sumarPrimos (n-1)