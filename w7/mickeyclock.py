import pygame
import datetime

pygame.init()
w = 600
h = 400
angle1 = 0
angle2 = 0

f_sys = pygame.font.SysFont('twcen',30)

sc = pygame.display.set_mode((w,h),pygame.RESIZABLE)

white = (255,255,255)

sc.fill(white) #fiiling the screen with white 

mickey_surf = pygame.image.load("image\mickey_clock.png") #doing the mickey surface 
lh_surf = pygame.image.load("image\mickey_left.png").convert_alpha() #left hand image 
rh_surf = pygame.image.load("image\mickey_right.png").convert_alpha() #right hand image 

mickey_surf = pygame.transform.scale(mickey_surf, (mickey_surf.get_width()//2.7 , mickey_surf.get_height()//2.7))
clock = pygame.time.Clock()
x=0

while 1:
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            exit()
    t = datetime.datetime.now()

    angle1 = -t.second*6
    angle2 = -t.minute *6

    sc_f_sys = f_sys.render(f'{t:%H-%M-%S}', 1 , (0,0,0),(255,255,255))
    
    lh_surf1 = pygame.transform.rotate(lh_surf, angle1)
    rh_surf1 = pygame.transform.rotate(rh_surf,angle2)
    
    rh_surf1=pygame.transform.scale(rh_surf1,(rh_surf1.get_width()//1.2 ,rh_surf1.get_height()//1.5))
    lh_surf1=pygame.transform.scale(lh_surf1,(lh_surf1.get_width()//1.2 , lh_surf1.get_height()//1.5))

    mickeyrect = mickey_surf.get_rect(center = (w//2,h//2))

    lh_rect = lh_surf1.get_rect(center = (w//2,h//2))
    rh_rect = rh_surf1.get_rect(center = (w//2,h//2))
    
    sc.blit(mickey_surf,mickeyrect)
    sc.blit(lh_surf1,lh_rect)
    sc.blit(rh_surf1,rh_rect)
    sc.blit(sc_f_sys,(10,10))    

    x-=1
    pygame.display.update()
    clock.tick(60)