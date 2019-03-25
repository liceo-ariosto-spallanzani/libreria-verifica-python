from spalla import Verifica

Verifica.url = "http://localhost:8080"
Verifica.firma("Giovanni Bruno")

es = Verifica.inizia_esercizio(2)
print(es)

es.consegna(es.dati ** 2)
