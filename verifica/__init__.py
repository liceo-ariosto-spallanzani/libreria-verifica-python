class Esercizio:
  def __init__(self, numero, ip, port):
    self.numero = numero
    self.ip = ip
    self.port = port
    
    self.consegna = requests.get(self.__get_url("consegna"),)

    def __get_url(path):
      return self.url = "{}:{}/{}".format(ip, port, path)

class Verifica:
  def __init__(self, nome, cognome, ip="192.168.1.231", port=8080):
    self.nome = nome
    self.cognome = cognome
    self.ip = ip
    self.port = port

  def esercizio(self, numero):
