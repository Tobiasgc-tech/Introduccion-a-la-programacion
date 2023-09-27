--Ejercio1--
contarVotosEnBlanco :: [(String, String)] -> [Int] -> Int -> Int
contarVotosEnBlanco [] _ _  = 0
contarVotosEnBlanco candidatos votos votostotales = votostotales - sumarVotos votos

sumarVotos :: [Int] -> Int
sumarVotos [] = 0
sumarVotos (x:xs) = x + sumarVotos xs

--Ejercio2--
tuplasConAlgunComIgual :: [(String, String)] -> Bool
tuplasConAlgunComIgual [] = False
tuplasConAlgunComIgual [x] = False
tuplasConAlgunComIgual ((a,b):(c,d):l) | a == c || a == d || b == c || b == d = True
                                       | otherwise = tuplasConAlgunComIgual ((a,b):l) || tuplasConAlgunComIgual ((c,d):l)

tuplasRepetidas:: [(String, String)] -> Bool
tuplasRepetidas [] = False
tuplasRepetidas [x] = False
tuplasRepetidas (x:y:l) | x == y = True
                        | (fst x == fst y || fst x == snd y) && (snd x == fst y || snd x == snd y) = True
                        | otherwise = tuplasRepetidas (x:l) && tuplasRepetidas (y:l)

tuplasConComponentesIguales :: [(String, String)] -> Bool
tuplasConComponentesIguales [] = False
tuplasConComponentesIguales (x:xs) | fst x == snd x = True
                                   | otherwise = tuplasConComponentesIguales xs

relacionesValidas :: [(String, String)] -> Bool
relacionesValidas l = not (tuplasRepetidas l || tuplasConComponentesIguales l || tuplasConAlgunComIgual l)