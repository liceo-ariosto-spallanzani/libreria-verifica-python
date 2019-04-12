class Fg: 
    rs="\033[00m"
    black='\033[30m'
    red='\033[31m'
    green='\033[32m'
    orange='\033[33m'
    blue='\033[34m'
    purple='\033[35m'
    cyan='\033[36m'
    lightgrey='\033[37m'
    darkgrey='\033[90m'
    lightred='\033[91m'
    lightgreen='\033[92m'
    yellow='\033[93m'
    lightblue='\033[94m'
    pink='\033[95m'
    lightcyan='\033[96m'


class Bg: 
    rs="\033[00m"
    black='\033[40m'
    red='\033[41m'
    green='\033[42m'
    yellow='\033[43m'
    blue='\033[44m'
    magenta='\033[45m'
    cyan='\033[46m'
    white='\033[47m'


class Directions:
  N = 0
  S = 1
  W = 2
  E = 3


class Entity:
  def __init__(self, graphic, game, x, y, fg_color, bg_color):
    self.graphic = graphic
    self.game = game
    self.x = x
    self.y = y
    self.fg_color = fg_color
    self.bg_color = bg_color if bg_color is not None else game.bg_color

  def __str__(self):
    return "{}{} {} {}{}".format(self.fg_color, self.bg_color, self.graphic, Bg.rs, Fg.rs)


class Player(Entity):
  def __init__(self, game, x, y):
    self.tail = [(x, y)]
    Entity.__init__(self, "*", game, x, y, Fg.blue, Bg.blue)
    self.tail_color = self.bg_color

  def move(self, direction):
    if self.game.status == Game.RUNNING:
      next_x = self.x
      next_y = self.y
      if direction == Directions.N and self.y > 0:
        next_y -= 1
      elif direction == Directions.S and self.y < self.game.h -1:
        next_y += 1
      elif direction == Directions.W and self.x > 0:
        next_x -= 1
      elif direction == Directions.E and self.x < self.game.w -1:
        next_x += 1

      e = self.game.get_entity_at_coords(next_x, next_y)

      self.x = next_x
      self.y = next_y
      if e is None:
        self.tail.append((self.x, self.y))
      else:
        self.bg_color = e.bg_color
        if type(e) is Obstacle:
          self.game.status = Game.GAME_OVER
        elif type(e) is Gold:
          self.game.status = Game.WIN

class Obstacle(Entity):
  def __init__(self, game, x, y):
    Entity.__init__(self, " ", game, x, y, Fg.lightgrey, Bg.black)
    

class Gold(Entity):
  def __init__(self, game, x, y):
    Entity.__init__(self, "$", game, x, y, Fg.yellow, Bg.yellow)

    
class Game:
  RUNNING = 0
  GAME_OVER = 1
  WIN = 2

  def __init__(self, level):
    self.__level = level -1
    self.__player = Player(self, 1, 1)
    self.__entities = [self.__player]
    self.__bg_color = Bg.green
    self.status = Game.RUNNING

    rows = ["#####\n", "#   #\n", "# $ #\n", "#####\n"]

    self.h = len(rows)
    self.w = len(rows[0]) -1

    for y in range(self.h):
      for x in range(self.w):
        char = rows[y][x]
        if char == "$":
          self.__entities.append(Gold(self, x, y))
        elif char != " ":
          self.__entities.append(Obstacle(self, x, y))

  def move_up(self):
    self.__player.move(Directions.N)

  def move_down(self):
    self.__player.move(Directions.S)

  def move_left(self):
    self.__player.move(Directions.W)

  def move_right(self):
    self.__player.move(Directions.E)

  def get_entity_at_coords(self, x, y):
    for e in self.__entities:
      if e.x == x and e.y == y: 
        return e   

  def go(self):
    print(self)

    if self.status == Game.WIN:
      print("{}Hai vinto!{}".format(Fg.green, Fg.rs))
    elif self.status == Game.GAME_OVER:
      print("{}Hai perso!{}".format(Fg.red, Fg.rs))

  def __str__(self):
    out = ""
    for y in range(self.h):
      for x in range(self.w):
        e = self.get_entity_at_coords(x, y)
        if e is not None:
          out += str(e)
        elif (x, y) in self.__player.tail:
          out += "{}   {}".format(self.__player.tail_color, Bg.rs)
        else:
          out += "{}   {}".format(self.__bg_color, Bg.rs)

      out += "\n"

    return out
