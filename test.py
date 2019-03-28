from spalla import Verifica

Verifica.url = "http://localhost:8080"
Verifica.firma("Giovanni Bruno")

es = Verifica.inizia_esercizio(3)

print(es)
