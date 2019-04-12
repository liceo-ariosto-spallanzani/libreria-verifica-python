'''
from spalla import Verifica

Verifica.url = "http://localhost:8080"
Verifica.firma("Giovanni Bruno")

es = Verifica.inizia_esercizio(3)

print(es)
'''

from spalla.Game import Game

g = Game(1)
g.move_right()
#g.move_down()
g.move_right()
g.move_right()
g.move_down()
g.move_left()
g.go()
