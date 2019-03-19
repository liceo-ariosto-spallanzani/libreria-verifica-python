from verifica import Verifica

Verifica.url = "http://localhost:8080"
Verifica.firma("Giovanni", "Bruno")

Verifica.stampa_esercizi()

es = Verifica.inizia_esercizio(1)
print(es)

es.consegna(sum(es.dati))
Verifica.stampa_voto()
