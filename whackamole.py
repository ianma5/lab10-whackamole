import pygame

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            draw_rows(screen)
            draw_cols(screen)
            
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

def draw_rows(screen):
    for row in range(16):
        print("hi")
        pygame.draw.line(screen, (255,255,255), (0,row*32), (640,row*32))
def draw_cols(screen):
    for col in range(20):
        print("hi")
        pygame.draw.line(screen, (255,255,255), (col*32,0), (col*32,512))

if __name__ == "__main__":
    main()
