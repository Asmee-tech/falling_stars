import pgzrun
from random import randint
WIDTH=1000
HEIGHT=800
s=Actor("star.png")
b=Actor("basket.png")
b.pos=500,740
score=0
def place_star():
    s.x=randint(50,WIDTH-50)
    s.y=0
def draw():
  screen.fill("navy")
  s.draw()
  b.draw()
  screen.draw.text(str(score),(5,5),fontsize=40,color="pink")
def update():
  global score
  s.y+=10
  if s.y>800:
    place_star()
  if keyboard.left:
    b.x-=10
  if keyboard.right:
    b.x+=10
  if s.colliderect(b):
    score+=1
    place_star()
place_star()
pgzrun.go()