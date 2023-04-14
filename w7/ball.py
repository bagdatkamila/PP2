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
        
        
        """if self.rect.left < 0:
        self.rect.left = 0
    if self.rect.right > SCREEN_WIDTH:
        self.rect.right = SCREEN_WIDTH
    if self.rect.top <= 0:
        self.rect.top = 0
    if self.rect.bottom >= SCREEN_HEIGHT:
        self.rect.bottom = SCREEN_HEIGHT
        """
        
        screen.fill((255, 255, 255))
        color = (255, 0, 255)
        pygame.draw.circle(screen, color, (x, y), 25)
        
        pygame.display.flip()
        clock.tick(20)