import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_RADIUS
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from shot import Shot

from asteroidfield import AsteroidField

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    asteroidField = AsteroidField()

    player = Player(SCREEN_WIDTH /2 , SCREEN_HEIGHT /2)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    

    
    while(1):
        log_state()

        updatable.update(dt)

        for ast in asteroids:
            if(ast.collides_with(player)):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            
            for shot in shots:
                if(shot.collides_with(ast)):
                    log_event("asteroid_shot")
                    shot.kill()
                    ast.split()

         

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        

        #player.update(dt)

        screen.fill("black")
        #player.draw(screen)
        for dr in drawable:
            dr.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()