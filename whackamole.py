import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_position_x = 0
        mole_position_y = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light blue")
            p = 32
            for i in range(20):
                pygame.draw.line(screen, "black", (p, 0), (p,  512))
                pygame.draw.line(screen, "black", (0, p), (640, p))
                p += 32
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mole_position_x <= event.pos[0] <= mole_position_x + 32:
                    if mole_position_y <= event.pos[1] <= mole_position_y + 32:
                        mole_position_x = random.randrange(0, 609, 32)
                        mole_position_y = random.randrange(0, 482, 32)
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_position_x, mole_position_y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
