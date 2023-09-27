tuplasRepetidas:: [(String, String)] -> Bool
tuplasRepetidas [] = True
tuplasRepetidas [x] = True
tuplasRepetidas (x:y:l) | x == y = False
                        | (fst x == fst y || fst x == snd y) && (snd x == fst y || snd x == snd y) = False
                        | otherwise = tuplasRepetidas (x:l) && tuplasRepetidas (y:l)

tuplasConComponentesIguales :: [(String, String)] -> Bool
tuplasConComponentesIguales [] = False
tuplasConComponentesIguales (x:xs) | fst x == snd x = True
                                   | otherwise = tuplasConComponentesIguales xs

relacionesValidas:: [(String, String)] -> Bool
relacionesValidas l = tuplasRepetidas l && not (tuplasConComponentesIguales l)

repetidas :: [(String, String)] -> [String]
repetidas [] = []
repetidas ((a, b):l) = [a, b] ++ repetidas l

sacarRepetidos :: (Eq t) => [t] -> [t]
sacarRepetidos [] = []
sacarRepetidos [x] = [x]
sacarRepetidos (x:xs) | x `elem` xs = sacarRepetidos xs
                      | otherwise = x:sacarRepetidos xs

personas :: [(String, String)] -> [String]
personas [] = []
personas [(a, b)] = [a, b]
personas x = sacarRepetidos (repetidas x)

amigosDe :: String -> [(String, String)] -> [String]
amigosDe _ [] = []
amigosDe x ((y,z):ys) | x == y = z:amigosDe x ys
                      | x == z = y:amigosDe x ys
                      | otherwise = amigosDe x ys