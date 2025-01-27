# this allows us to use code from
# the open-source pygame library
# throughout this file
from player import Player
from constants import SCREEN_WIDTH,SCREEN_HEIGHT
import pygame # type: ignore

# Initialice Pygame

def main():
    dt = 0
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
        
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0))

        for updatable_obj in updatable:
            updatable_obj.update(dt)

        for drawable_obj in drawable:
            drawable_obj.draw(screen)

        # player.draw(screen)
        # player.update(dt)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()