from spalla.Game import Game
Game.url = "http://localhost:8081"

Game.sign("Giovanni Bruno")

player = Game.start_level(3)
player.move()
player.move()
player.turn_right()
player.move()
player.go()
