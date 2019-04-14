
from spalla.Game import Game
Game.url = "http://localhost:8080"

# Game.sign("Giovanni Bruno")

level = Game.start_level(1)

level.move_right()
level.move_right()
level.move_right()

level.play()
