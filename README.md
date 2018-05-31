# PyGame wrapper for beginner.

![screenshot.png](screenshot.png)

## Sample Code

```python
import gamesys

# create new window that title is 'GUNMAN'. default FPS is 2.
game = gamesys.init('GUNMAN', 2)

# load image file. this gunman variable is a PyGame surface object.
gunman = game.load(game.file('gunman01.png'))

while True:
  # draw a surface to center of window.
  game.draw(gunman, 448, 320)

  # update screen.
  game.update()
```

## References

### gamesys.init(windowTitle, FPS, windowSize) => GameSys

  ウインドウを作成します。
  初期値は、FPSが2、windowSizeは横1024、縦768です。windowSizeはタプルで指定します。

  ```python
  import gamesys
  game = gamesys.init('GUNMAN', 30, (480, 320))

  while True:
      game.update()
  ```

### game.draw(surface, x, y)

  画面に画像(サーフェース)を描画します。

  ```python
  import gamesys
  game = gamesys.init('GUNMAN')
  gunman = game.load(game.file('gunman01.png'))

  while True:
    game.draw(gunman, 448, 320)
    game.update()
  ```

### game.fillRect(color, rect)

  画面に四角を描画します。

  ```python
  import gamesys
  game = gamesys.init('GUNMAN')

  while True:
    game.fillRect((255, 0, 0), (480, 320, 128, 128))
    game.update()
  ```

### game.load(filename) => pygame.Surface

  画像を読み込みます。

  ```python
  import gamesys
  game = gamesys.init('GUNMAN')
  gunman = game.load(game.file('gunman01.png'))

  while True:
    game.draw(gunman, 448, 320)
    game.update()
  ```

### game.surface(size) => pygame.Surface

  四角の画像(サーフェース)を作成します。

  ```python
  import gamesys
  game = gamesys.init('GUNMAN')
  redBlock = game.fill(game.surface((128, 128)), (255, 0, 0), (0, 0, 128, 128))

  while True:
    game.draw(redBlock, 448, 320)
    game.update()
  ```

### game.fill(surface, color, rect) => pygame.Surface

  画像(サーフェース)の一部を四角で塗りつぶします。

  ```python
  import gamesys
  game = gamesys.init('GUNMAN')
  gunman = game.load(game.file('gunman01.png'))

  while True:
    game.draw(game.fill(gunman, (255, 0, 0), (0, 0, 32, 32)), 448, 320)
    game.update()
  ```

### game.resize(surface, size) => pygame.Surface

  画像(サーフェース)のサイズを変更します。

  ```python
  import gamesys
  game = gamesys.init('GUNMAN')
  gunman = game.load(game.file('gunman01.png'))

  while True:
    game.draw(game.resize(gunman, (512, 256)), 256, 256)
    game.update()
  ```

### game.rotate(surface, rotate) => pygame.Surface

  画像(サーフェース)を回転させます。

  ```python
  import gamesys
  game = gamesys.init('GUNMAN')
  gunman = game.load(game.file('gunman01.png'))

  while True:
    game.draw(game.rotate(gunman, 30), 448, 420)
    game.update()
  ```

### game.scale(surface, scale) => pygame.Surface

  画像(サーフェース)の拡大縮小させます。

  ```python
  import gamesys
  game = gamesys.init('GUNMAN')
  gunman = game.load(game.file('gunman01.png'))

  while True:
    game.draw(game.scale(gunman, 2), 384, 256)
    game.update()
  ```

### game.file(filename) => String

  リソースフォルダ内のファイルのファイルパスを返します。
  ゲームに使用する画像やサウンド関連のファイルは、resourcesフォルダに入れます。

### game.key(keyCode) => Bool

  キーが押されているかどうかを調べる。押されていれば True を返す。
  使用可能なキーコードは以下の通り

  - game.KEY_UP
  - game.KEY_DOWN
  - game.KEY_LEFT
  - game.KEY_RIGHT
  - game.KEY_SPACE

```python
import gamesys
game = gamesys.init('GUNMAN')

while True:
  if game.key(game.KEY_SPACE):
    print('スペースキー ON')
  else:
    print('スペースキー OFF')
  game.update()
```

### game.music(musicFilePath) => Music

```python
import gamesys
game = gamesys.init('GUNMAN')
music = game.music(game.file('main_theme.ogg'))

# BGMの再生
music.play()

# BGMの停止
# music.stop()

while True:
  game.update()
```

### game.sound(soundFilePath) => pygame.mixer.Sound

```python
import gamesys
game = gamesys.init('GUNMAN')
sound = game.sound(game.file('coin.ogg'))

# 効果音の再生
sound.play()

while True:
  game.update()
```

### game.update(bgColor)

画面を更新します。bgColorで背景色を指定できます。省略した場合は白で塗りつぶします。

```python
import gamesys
game = gamesys.init('GUNMAN')

while True:
  game.update((0, 255, 0))
```
