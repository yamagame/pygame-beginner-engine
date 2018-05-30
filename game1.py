import gamesys

game = gamesys.init('GUNMAN')
gunman = game.load(game.file('gunman01.png'))

while True:
  game.draw(gunman, 448, 320)
  game.update()
