import gamesys

game = gamesys.init('GUNMAN', 30)
gunmanUP = game.load(game.file('gunman01.png'))
gunmanDOWN = game.load(game.file('gunman02.png'))

y = 320

while True:
  if game.key(game.KEY_UP):
    y = y - 4
  if game.key(game.KEY_DOWN):
    y = y + 4
  game.draw(gunmanUP, 448, y)
  game.update()
