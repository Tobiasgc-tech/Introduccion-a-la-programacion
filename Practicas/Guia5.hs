--GUIA 5
--Ejercio1.1
{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use foldr" #-}
longitud :: [t] -> Int
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

--Ejercio1.2
ultimo :: [t] -> t
ultimo [x] = x
ultimo x = ultimo (tail x)

--Ejercio1.3
principio :: [Int] -> [Int]
principio x = [head x,0,ultimo x]

--Ejercio1.4
reverso :: [t] -> [t]
reverso [] = []
reverso (x:xs) = reverso xs ++ [x]

--Ejercio2.1
pertenece :: Eq t => t -> [t] -> Bool
pertenece _ [] = False
pertenece n (x:xs) | n == x = True
                   | otherwise = pertenece n xs

--Ejercio2.2
todosIguales :: Eq t => [t] -> Bool
todosIguales [] = True
todosIguales [_] = True
todosIguales (x:xs) | x == head xs = todosIguales xs
                    | otherwise = False

--Ejercio2.3
todosDistintos :: Eq t => [t] -> Bool
todosDistintos [] = True
todosDistintos [x] = True
todosDistintos (x:xs) | x /= head xs = todosDistintos xs
                      | otherwise = False

--Ejercio2.4
hayRepetidos :: [Int] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs) | pertenece x  xs = True
                    | otherwise = hayRepetidos xs

--Ejercio2.5
quitar :: Eq t => t -> [t] -> [t]
quitar _ [] = []
quitar n (x:xs) | n == x = xs
                | otherwise = x : quitar n xs

--Ejercio2.6
quitarTodos :: Eq t => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos n (x:xs) | n == x = quitarTodos n xs
                     | n /= x = x : quitarTodos n xs

--Ejercio2.7
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) = x : eliminarRepetidos (quitarTodos x xs)

--Ejercio2.8
mismoElemento :: (Eq t) => [t] -> [t] -> Bool
mismoElemento [] [] = True
mismoElemento _ [] = False
mismoElemento [] _ = False
mismoElemento (x:xs) l | pertenece x l = mismoElemento (eliminarRepetidos xs) (quitarTodos x l)
                       | otherwise = False

--Ejercio2.9
capicuaL :: (Eq t) => [t] -> Bool
capicuaL [] = True
capicuaL l = l == reverso l

--Ejercio3.1
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

--Ejercio3.2
productoria :: [Integer] -> Integer
productoria [] = 1
productoria (x:xs) = x * productoria xs

--Ejercio3.3
maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x:y:xs) | x > y = maximo (x:xs)
                | otherwise = maximo (y:xs)

--Ejercio3.4
sumarN :: Integer -> [Integer] -> [Integer]
sumarN _ [] = []
sumarN n (x:xs) = n + x : sumarN n xs

--Ejercio3.5
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero [] = []
sumarElPrimero (x:xs) = sumarN x (x:xs)

--Ejercio3.6
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo [] = []
sumarElUltimo (x:xs) = sumarN (ultimo xs) (x:xs)

pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs) | mod x  2 == 0 = x : pares xs
             | otherwise = pares xs

multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN _ [] = []
multiplosDeN n (x:xs) = n * x : multiplosDeN n xs

--Ejercio3.9
ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar l = minimo l : ordenar (quitar (minimo l) l)

minimo :: [Integer] -> Integer
minimo [x] = x
minimo (x:y:xs) | x < y = minimo (x:xs)
                | otherwise = minimo (y:xs)

--Ejercio4.1
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos (x:y:xs) | x==y && x==' ' = sacarBlancosRepetidos (y:xs)
                               | otherwise = x : sacarBlancosRepetidos (y:xs)

--Ejercio4.2
contarPalabras :: [Char] -> Integer
contarPalabras [] = 0
contarPalabras xs = contarBlancos (sacarBlancoIniFin ( sacarBlancosRepetidos xs)) + 1

contarBlancos :: [Char] -> Integer
contarBlancos [] = 0
contarBlancos (x:xs) | x == ' ' = 1 + contarBlancos xs
                     | otherwise = contarBlancos xs

sacarBlancoIniFin :: [Char] -> [Char]
sacarBlancoIniFin [] = []
sacarBlancoIniFin (x:xs) | x == ' '  = sacarBlancoIniFin xs
                            | head (reverso xs) == ' ' = sacarBlancoIniFin (quitarElUltimo (x:xs))
                            | otherwise = x:xs

quitarElUltimo :: (Eq t) => [t] -> [t]
quitarElUltimo [] = []
quitarElUltimo [x] = []
quitarElUltimo (x:xs) = x : quitarElUltimo xs

--Ejercio4.3
palabras :: [Char] -> [[Char]]
palabras xs = armarListaPalabras (sacarBlancosRepetidos (sacarBlancoIniFin xs))

armarListaPalabras :: [Char] -> [[Char]]
armarListaPalabras [] = []
armarListaPalabras xs = primerPalabra xs : armarListaPalabras (sacarPrefijo (primerPalabra xs) xs)

primerPalabra :: [Char] -> [Char]
primerPalabra [] = []
primerPalabra [' '] = []
primerPalabra [x] = [x]
primerPalabra (x:' ':xs) = [x]
primerPalabra (x:y:xs) = x : primerPalabra (y:xs)

sacarPrefijo :: [Char] -> [Char] -> [Char]
sacarPrefijo [] [] = []
sacarPrefijo [] (y:ys) | y==' ' = ys
                       | otherwise = y:ys
sacarPrefijo (x:xs) (y:ys) | x==y = sacarPrefijo xs ys
                           | y==' ' = ys
                           | otherwise = ys

--Ejercio4.4
palabraMasLarga :: [Char] -> [Char]
palabraMasLarga xs = sacarBlancosRepetidos (sacarBlancoIniFin (palabraMasLargaAux xs))

palabraMasLargaAux :: [Char] -> [Char]
palabraMasLargaAux xs | sacarPrimeraPalabra xs == [] = primerPalabra xs
                      | contarLetrasDeUnaPalabra (primerPalabra xs) > contarLetrasDeUnaPalabra (palabraMasLargaAux (sacarPrimeraPalabra xs)) = primerPalabra xs
                      | otherwise = palabraMasLargaAux (sacarPrimeraPalabra xs)

contarLetrasDeUnaPalabra :: [Char] -> Integer
contarLetrasDeUnaPalabra [] = 0
contarLetrasDeUnaPalabra (x:xs) = 1 + contarLetrasDeUnaPalabra xs

sacarPrimeraPalabra :: [Char] -> [Char]
sacarPrimeraPalabra [] = []
sacarPrimeraPalabra (x:xs) | x == ' ' = xs
                           | otherwise = sacarPrimeraPalabra xs

--Ejercio4.5
aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar (x:xs) = x ++ aplanar xs

--Ejercio4.6
aplanarConBlancos :: [[Char]] -> [Char]
aplanarConBlancos [] = []
aplanarConBlancos (x:xs) = x ++ " "  ++ aplanar xs

--Ejercio4.7
aplanarConNBlancos :: [[Char]] -> Integer -> [Char]
aplanarConNBlancos [] _ = []
aplanarConNBlancos [x] _ = x
aplanarConNBlancos (x:xs) n = x ++ agregarBlancos n ++ aplanarConNBlancos xs n

agregarBlancos :: Integer -> [Char]
agregarBlancos 0 = []
agregarBlancos n = ' ' : agregarBlancos (n-1)