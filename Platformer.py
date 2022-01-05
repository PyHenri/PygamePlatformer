import pygame,sys

pygame.init()
Clock = pygame.time.Clock()
FPS = 60
size = [800,600]
bg = [0,0,0]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('classes in pygame')


class Player:
    def __init__(self,vel,x,y,width=50,height=100):  #init the player
      self.vel = vel
      self.vel_y = 16
      self.vel_y2 = 0
      self.vx = 0
      self.vy = 0
      self.x = x
      self.y = y
      self.width = width
      self.height = height
      self.jump = False
      self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
    def move(self):
      k = pygame.key.get_pressed()
      if k[pygame.K_LEFT]:  #go left
        self.vx = -self.vel
      if k[pygame.K_RIGHT]:  #go right
        self.vx = self.vel
      if k[pygame.K_UP] and self.vel_y == 16:  #checking conditions for jumping
        self.jump = True
      if self.jump:   #jump
        if self.vel_y >= -16:
          self.vy = -self.vel_y
          self.vel_y -= 1
        else:
          self.jump = False
          self.vel_y = 16
      if self.jump == False:  #gravity is only enabled when the player is not jumping
        self.vel_y2 += 1
        if self.vel_y2 > 10:
          self.vel_y2 = 10
        self.vy += self.vel_y2
      for block in blocks:   #get data of every block
        if block.Platform.colliderect(self.x + self.vx, self.y, self.width, self.height): #checking x collision
          self.vx = 0
        if block.Platform.colliderect(self.x, self.y + self.vy, self.width, self.height): #checking y collision
          self.vy = 0
          if block.Platform.y > self.y: #prevents a bug that makes the player jump through the block below
            self.y += block.Platform.top-self.rect.bottom  #remove remaining distance between floor and player
      self.x += self.vx #adding velocity to coordinates
      self.y += self.vy
      self.vx = 0
      self.vy = 0
      self.rect = pygame.Rect(self.x,self.y,self.width,self.height)  #player rect
    def draw(self): #draw the player
      self.figur = pygame.draw.rect(screen,(255,255,255),(self.x,self.y,self.width,self.height))
    def do(self):
      self.move()
      self.draw()
        
class Object:
  def __init__(self,x,y,width,height,color):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.color = color
  def draw(self): #drawing the block
    self.Platform = pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height))

player = Player(2,350,5) #setting up the level
blocks = list()
blocks.append(Object(650,400,145,35,(255,0,255)))
blocks.append(Object(450,500,145,35,(255,0,255)))
blocks.append(Object(1,550,799,35,(255,0,255)))

while True:   #main
    screen.fill(bg)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
    for block in blocks:
      block.draw()
    player.do()
    Clock.tick(FPS)
    pygame.display.update()
