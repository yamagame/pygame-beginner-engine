import gamesys

game = gamesys.init('GUNMAN')
gunmanUP = game.load(game.file('gunman01.png'))
gunmanDOWN = game.load(game.file('gunman02.png'))

while True:
  game.draw(gunmanUP, 448, 320)
  game.update()
  game.draw(gunmanDOWN, 448, 320)
  game.update()
