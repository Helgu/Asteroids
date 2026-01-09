import pygame
import random
from logger import log_state, log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):

    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)
    
    def update(self,dt):
        self.position += (self.velocity*dt)

    def split(self):
        self.kill()
        if (self.radius <  ASTEROID_MIN_RADIUS):
            return
        log_event("asteroid_split")
        angle = random.uniform(20,50)
        new_first_dir = self.velocity.rotate(angle)
        new_second_dir = self.velocity.rotate(-angle)

        new_first = Asteroid(self.position.x,self.position.y,self.radius - ASTEROID_MIN_RADIUS)
        new_second = Asteroid(self.position.x,self.position.y,self.radius - ASTEROID_MIN_RADIUS)

        new_first.velocity = new_first_dir * 1.2
        new_second.velocity = new_second_dir * 1.2

