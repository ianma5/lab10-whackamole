import pygame
import random

def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        molepos = (0,0) # initial position is top left corner
        screen = pygame.display.set_mode((640, 512)) # 20x16, 32x32 squares
        square_size = 32
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if (event.pos[0]//square_size==molepos[0]//square_size) and (event.pos[1]//square_size==molepos[1]//square_size): # checks if mouseclick divided by square size is equalto random molepos
                        molepos = randomlocation(square_size) # sets the position so he is on a random square

            screen.fill("light green")
        
            #draws the rows and columns onto the screen
            draw_rows(screen, square_size)
            draw_cols(screen, square_size)
            # places/updates the mole somewhere on the screen
            screen.blit(mole_image, mole_image.get_rect(topleft=molepos))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

def draw_rows(screen, square_size):
    for row in range(16):
        pygame.draw.line(screen, (255,255,255), (0,row*square_size), (640,row*square_size))
def draw_cols(screen, square_size):
    for col in range(20):
        pygame.draw.line(screen, (255,255,255), (col*square_size,0), (col*square_size,512))
def randomlocation(square_size):
    row = random.randint(0,19)
    col = random.randint(0,15)
    return (row*square_size,col*square_size) # returns tuple multiplied by square size

if __name__ == "__main__":
    main()
