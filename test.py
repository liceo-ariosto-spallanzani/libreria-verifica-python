from verifica import Verifica

verifica = Verifica("Giovanni", "Bruno", "http://localhost")

esercizio = verifica.inizia_esercizio(2)
dati = esercizio.dati

m = min(dati)
for i in range(len(dati)):
    dati[i] *= m

esercizio.consegna(dati)
print(esercizio)


verifica.print_voto()

