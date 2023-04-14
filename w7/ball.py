import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
done = False
x = 30
y = 30

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3

        if x <= 0:
            x = 0
        elif y <= 0:
            y = 0
        elif y >= 600:
            y = 600
        elif x >= 600:
            x = 600
          
        screen.fill((0, 0, 0))
        color = (250, 0, 0)
        pygame.draw.circle(screen, color, (x, y), 25)
        
        pygame.display.flip()
        clock.tick(20)    