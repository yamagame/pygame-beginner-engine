import gamesys

game = gamesys.init('GUNMAN', 30)
gunman = game.load(game.file('gunman01.png'))

x = 448
y = 320

while True:
  if game.key(game.KEY_LEFT):
    x = x - 4
  if game.key(game.KEY_RIGHT):
    x = x + 4
  if game.key(game.KEY_UP):
    y = y - 4
  if game.key(game.KEY_DOWN):
    y = y + 4
  game.draw(gunman, x, y)
  game.update()
