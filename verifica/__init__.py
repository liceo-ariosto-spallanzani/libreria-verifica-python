import requests


class Esercizio:
    def __init__(self, verifica, numero, testo, dati):
        self.verifica = verifica
        self.numero = numero
        self.testo = testo
        self.dati = dati

    def consegna(self, risultato):
        r = requests.post(
            self.verifica.get_url("esercizi/{}".format(self.numero)),
            headers={"x-data": "True"},
            json={"data": risultato}
        ).json()

        print(r["status"])

    def __str__(self):
        return "{}\nDATI:\n{}".format(self.testo, self.dati)


class Verifica:
    def __init__(self, nome, cognome, ip="192.168.1.231", port=8080):
        self.nome = nome
        self.cognome = cognome
        self.ip = ip
        self.port = port

        self.__firma()

    def get_url(self, path):
        return "{}:{}/{}".format(self.ip, self.port, path)

    def __firma(self):
        requests.post(
            self.get_url("accreditamento"),
            json={"nome": "{} {}".format(self.nome.upper(), self.cognome.upper())}
        )

    def stampa_voto(self):
        r = requests.get(self.get_url("risultati"))
        print("{}/10".format(r.json()[0]["score"]))

    def inizia_esercizio(self, numero):
        r = requests.get(self.get_url("esercizi/{}".format(numero)), headers={"x-data": "True"}).json()

        return Esercizio(self, numero, r["message"], r["data"])
