use 5L_Merendine;

SELECT NomeMerenda, TipoMacchinetta, NomeScuola
FROM Merende, Posizioni, Macchinette, Scuole
WHERE Merende.CodMerenda = Posizioni.CodMer
AND Posizioni.CodMac = Macchinette.CodMacchinetta
AND Macchinette.CodSc = Scuole.CodScuola
AND Scuole.CodScuola = '34'
ORDER BY Prezzo DESC;

SELECT NomeMerenda, TipoMacchinetta, QtaMerendine, NomeScuola
FROM Merende, Posizioni, Macchinette, Scuole
WHERE Merende.CodMerenda = Posizioni.CodMer
AND Posizioni.CodMac = Macchinette.CodMacchinetta
AND Macchinette.CodSc = Scuole.CodScuola
AND QtaMerendine > 0
ORDER BY NomeScuola ASC, QtaMerendine DESC;

SELECT CodMacchinetta
FROM Posizioni, Macchinette
WHERE Posizioni.CodMac = Macchinette.CodMacchinetta
AND QtaMerendine = 0;

SELECT CodMacchinetta
FROM Posizioni, Macchinette
WHERE Posizioni.CodMac = Macchinette.CodMacchinetta
AND QtaMerendine = 0
GROUP BY CodMacchinetta;

SELECT NomeScuola, COUNT(DISTINCT CodMacchinetta) AS NumeroMacchinette
FROM Scuole, Macchinette
WHERE Scuole.CodScuola = Macchinette.CodSc
GROUP BY NomeScuola;

SELECT AVG(Prezzo) AS PrezzoMedio
FROM Merende, Posizioni, Macchinette, Scuole
WHERE Merende.CodMerenda = Posizioni.CodMer
AND Posizioni.CodMac = Macchinette.CodMacchinetta
AND Macchinette.CodSc = Scuole.CodScuola
AND NomeScuola = 'scA';

SELECT CodMacchinetta
FROM Posizioni, Macchinette
WHERE Posizioni.CodMac = Macchinette.CodMacchinetta
AND QtaMerendine = 0
GROUP BY CodMacchinetta
HAVING COUNT(*) = (SELECT COUNT(*) FROM Merende);

SELECT TipoMacchinetta, SUM(QtaMerendine) AS TotaleMerendine
FROM Posizioni, Macchinette
WHERE Posizioni.CodMac = Macchinette.CodMacchinetta
GROUP BY TipoMacchinetta
HAVING TotaleMerendine >= 40;
SELECT CodMacchinetta, NomeScuola, SUM(Prezzo * QtaMerendine) AS TotalePrezzi
FROM Merende, Posizioni, Macchinette, Scuole
WHERE Merende.CodMerenda = Posizioni.CodMer
AND Posizioni.CodMac = Macchinette.CodMacchinetta
