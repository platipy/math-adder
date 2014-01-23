import spyral
import random
import math

WIDTH = 1200
HEIGHT = 900
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (1200, 900)

class Ball(spyral.Sprite):
    def __init__(self, scene):
        super(Ball, self).__init__(scene)
        self.image = spyral.Image(size=(20, 20))
        self.image.draw_circle(WHITE, (10, 10), 10)
        
        scene.register("pong_score", self._reset)
        scene.register("director.update", self.update)
        self._reset()
        
    def _reset(self):
        theta = random.random()*2*math.pi
        while ((theta > math.pi/4 and theta < 3*math.pi/4) or
               (theta > 5*math.pi/4 and theta < 7*math.pi/4)):
            theta = random.random()*2*math.pi
        r = 300
        
        self.vel_x = r * math.cos(theta)
        self.vel_y = r * math.sin(theta)
        self.anchor = 'center'
        self.pos = (WIDTH/2, HEIGHT/2)
                
    def update(self, dt):
        self.x += dt * self.vel_x
        self.y += dt * self.vel_y
        
        r = self.get_rect()
        if r.top < 0:
            r.top = 0
            self.vel_y = -self.vel_y
        if r.bottom > HEIGHT:
            r.bottom = HEIGHT
            self.vel_y = -self.vel_y
        
        self.pos = r.center
        
        if r.left < 0:
            self.scene._handle_event("pong_score", spyral.Event(side='left'))
        if r.right > WIDTH:
            self.scene._handle_event("pong_score", spyral.Event(side='right'))
            
    def collide_paddle(self, paddle):
        if self.collide_sprite(paddle):
            self.vel_x = -self.vel_x

class Paddle(spyral.Sprite):
    def __init__(self, scene, side):
        spyral.Sprite.__init__(self, scene)
        self.image = spyral.Image(size=(20, 300)).fill((255, 255, 255))
        if side == 'left':
            self.anchor = 'midleft'
            self.x = 20
        else:
            self.anchor = 'midright'
            self.x = WIDTH - 20
        self.y = HEIGHT/2
        self.side = side
        self.moving = False
        
        up = 'w' if self.side == 'left' else "up"
        down = 's' if self.side == 'left' else "down"
        
        scene.register("input.keyboard.down."+up, self.move_up)
        scene.register("input.keyboard.down."+down, self.move_down)
        scene.register("input.keyboard.up."+up, self.stop_move)
        scene.register("input.keyboard.up."+down, self.stop_move)
        scene.register("director.update", self.update)
        scene.register("pong_score", self._reset)
        
    def move_up(self):
        self.moving = 'up'
    def move_down(self):
        self.moving = 'down'
    def stop_move(self):
        self.moving = False
    def _reset(self):
        self.y = HEIGHT/2
        
    def update(self, dt):
        paddle_velocity = 250
        
        if self.moving == 'up':
            self.y -= paddle_velocity * dt
        elif self.moving == 'down':
            self.y += paddle_velocity * dt
                
        r = self.get_rect()
        if r.top < 0:
            r.top = 0
        if r.bottom > HEIGHT:
            r.bottom = HEIGHT
            
        #self.pos == getattr(r, self.anchor)


class Pong(spyral.Scene):
    def __init__(self, *args, **kwargs):
        global manager
        spyral.Scene.__init__(self, SIZE)
        self.background = spyral.Image(size=SIZE).fill(BG_COLOR)
        
        self.ball = Ball(self)
        self.left_paddle = Paddle(self, 'left')
        self.right_paddle = Paddle(self, 'right')
        
        self.register("system.quit", spyral.director.pop)
        self.register("director.update", self.update)
        self.register("input.keyboard.down.q", spyral.director.pop)
        
    def update(self, dt):
        self.ball.collide_paddle(self.left_paddle)
        self.ball.collide_paddle(self.right_paddle)
    