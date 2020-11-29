import pygame



def main():
    pygame.init()

    DISPLAY=pygame.display.set_mode((800,800),0,32)

    WHITE=(255,255,255)
    BLUE=(0,0,255)

    DISPLAY.fill(WHITE)

    pygame.draw.rect(DISPLAY,BLUE,(100,100,100,100))

    while True:
        # for event in pygame.event.get():
        #     if event.type==QUIT:
        #         pygame.quit()
        #         sys.exit()
        pygame.display.update()

main()

