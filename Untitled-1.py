import pygame

pygame.init()

screen_width = 1200
screen_height = 600

def main():
    game_clock = pygame.time.Clock()
    screen_size = (screen_width, screen_height)
    screen = pygame.display.set_mode(screen_size, 0, 32)
    background = pygame.image.load('png/BG.png').convert()
    while True:
        game_clock.tick(45)

        for event in pygame.event.get:
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.blit(pygame.transform.scale(background, screen_size), (0,0))
        pygame.display.flip


if __name__ == "__main__":
    main()