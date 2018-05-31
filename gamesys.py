import pygame, sys, random, os
from pygame.locals import *

# ウインドウを画面中央にする
os.environ['SDL_VIDEO_CENTERED'] = '1'

fpsClock = pygame.time.Clock()

class GameSys:
  TYPE_SURF = 'surface'
  TYPE_FILLRECT = 'fillrect'
  
  KEY_UP='KEY_UP'
  KEY_DOWN='KEY_DOWN'
  KEY_LEFT='KEY_LEFT'
  KEY_RIGHT='KEY_RIGHT'
  KEY_SPACE='KEY_SPACE'
  
  keyCode = {
    KEY_UP: K_UP,
    KEY_DOWN: K_DOWN,
    KEY_LEFT: K_LEFT,
    KEY_RIGHT: K_RIGHT,
    KEY_SPACE: K_SPACE,
  }

  # コンストラクタ
  def __init__(self, title, fps=2, size=(1024, 768)):
    pygame.init()
    self.screen = pygame.display.set_mode(size)
    pygame.display.set_caption(title)
    self.keyPressed = pygame.key.get_pressed();
    # フレームレート
    self.FPS = fps
    # キャラクタ用のリスト
    self.sprites = []
  
  # 画像の読み込み
  def load(self, filename):
    return pygame.image.load(filename).convert_alpha()
  
  # キャラクタの描画
  def draw(self, surface, x, y):
    self.sprites.append({ 'type': GameSys.TYPE_SURF, 'surface': surface, 'x': x, 'y': y})
  
  # 矩形の描画
  def fillRect(self, color=(255,255,255), rect=(0,0,32,32)):
    self.sprites.append({ 'type': GameSys.TYPE_FILLRECT, 'color': color, 'rect': rect})

  # Surfaceの作成
  def surface(self, size=(32, 32)):
    return pygame.Surface(size, pygame.SRCALPHA, 32).convert_alpha()
  
  # 矩形の塗りつぶし
  def fill(self, surface, color=(0,0,0), rect=(0,0,32,32), special_flags=0):
    surface.fill(color, rect, special_flags)
    return surface
  
  # キャラクタの上下左右反転
  def flip(self, surface, xbool=False, ybool=False):
    return pygame.transform.flip(surface, xbool, ybool)
  
  # キャラクタのサイズ
  def resize(self, surface, size=(32,32)):
    return pygame.transform.scale(surface, size)
  
  # キャラクタの回転
  def rotate(self, surface, rotate=0):
    return pygame.transform.rotozoom(surface, rotate, 1)
  
  # キャラクタの拡大縮小
  def scale(self, surface, scale=1):
    return pygame.transform.rotozoom(surface, 0, scale)

  # リソースファイルパス
  def file(self, filename):
    return os.path.join('resources', filename)
  
  # キー入力判定
  def key(self, keyCode):
    return self.keyPressed[self.keyCode[keyCode]]
  
  # BGM用
  def music(self, music):
    class Music:
      def __init__(self, music):
        self.music = music
      def play(self):
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.play()
      def stop(self):
        pygame.mixer.music.stop()
    return Music(music)
    
  # SFX用
  def sound(self, sound):
    return pygame.mixer.Sound(sound)
  
  # 画面の更新
  def update(self, bgColor=(255, 255, 255)):
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
    self.screen.fill(bgColor)
    for obj in self.sprites:
      if (obj['type'] == GameSys.TYPE_SURF):
        self.screen.blit(obj['surface'], (obj['x'], obj['y']))
      elif (obj['type'] == GameSys.TYPE_FILLRECT):
        self.screen.fill(obj['color'], obj['rect'])

    pygame.display.update()
    fpsClock.tick(self.FPS)
    self.sprites = []
    self.keyPressed = pygame.key.get_pressed();

def init(title, fps=2, size=(1024, 768)):
  return GameSys(title, fps, size)
