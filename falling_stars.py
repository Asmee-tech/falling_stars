import pgzrun
from random import randint
WIDTH=1000
HEIGHT=800
s=Actor("star.png")
b=Actor("basket.png")
b.pos=500,740
score=0
lives=10
game_over=False
def place_star():
    s.x=randint(50,WIDTH-50)
    s.y=0
def draw():
  screen.fill("navy")
  s.draw()
  b.draw()
  screen.draw.text(str(score),(5,5),fontsize=40,color="pink")
  screen.draw.text(str(lives),(955,5),fontsize=40,color="red")
  if game_over:
    screen.fill("white")
    screen.draw.text(("Game Over!"),(200,370),fontsize=150,color="red")
    screen.draw.text(str(score),(500,500),fontsize=80,color="blue")
def update():
  global score, lives
  s.y+=10
  if s.y>800:
    place_star()
  if keyboard.left:
    b.x-=10
  if keyboard.right:
    b.x+=10
  if s.colliderect(b) and not game_over:
    score+=1
    place_star()
  if s.y>798:
    lives-=1
    if lives==0:
      gameo()
    place_star()
def gameo():
  global game_over
  game_over=True
place_star()
pgzrun.go()
