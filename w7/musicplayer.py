import pygame
import sys
    
    
def main():
    pygame.init()
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
    screen = pygame.display.set_mode((350, 700))
    pygame.display.set_caption("Music Player")
    bg = pygame.image.load("C://Users//admin//OneDrive//Рабочий стол//pp2//w7//image//backround.png").convert_alpha()
    
    #пишем кнопки для начального экрана
    myfont = pygame.font.Font("C://Users//admin//OneDrive//Рабочий стол//pp2//w7//image//Roboto-Black.ttf", 60)
    text = myfont.render("sweater_weather_ready", False, (193, 196, 192))
    buttom_list = [
        text.get_rect(topleft=(10, 200)),
        text.get_rect(topleft=(10, 300)),
        text.get_rect(topleft=(10, 400))
    ]
    
    #photos of the songs
    song_counter = 0
    amount_of_songs = 3
    
    song_image_list = [
        pygame.image.load("C://Users//admin//OneDrive//Рабочий стол//pp2//w7//image//those_eyes.png").convert_alpha(),
        pygame.image.load("C://Users//admin//OneDrive//Рабочий стол//pp2//w7//image//is_there_smn_else.png").convert_alpha(),
        pygame.image.load("C://Users//admin//OneDrive//Рабочий стол//pp2//w7//image//tinnitus.png").convert_alpha()
    ]
        
    #about sounds
    songs_list = [
        pygame.mixer.Sound("C://Users//admin//OneDrive//Рабочий стол//pp2//w7//music//New West - Those eyes (Speed up).mp3"), 
        pygame.mixer.Sound("C://Users//admin//OneDrive//Рабочий стол//pp2//w7//music//The Weeknd - Is There Someone Else.mp3"),
        pygame.mixer.Sound("C://Users//admin//OneDrive//Рабочий стол//pp2//w7//music//txt-tinnitus-wanna-be-a-rock.mp3")
    ]


    x = 1
    song_is_play = False
    #использую для пробела, остановить при первом и если еще раз начать песню
    stop_sound = True
    while True:
        #для позиции мышки
        mouse = pygame.mouse.get_pos()
        #стартовый экран
        if not song_is_play:
            screen.blit(bg, (0, 0))
        else:
            screen.blit(song_image_list[song_counter], (0, 0))

        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            #обработка мышки
            if event.type == pygame.MOUSEBUTTONDOWN:
                for buttom in buttom_list:
                    if buttom.collidepoint(mouse) and not song_is_play:
                        song_counter = buttom_list.index(buttom)
                        songs_list[song_counter].play()
                        song_is_play = True

            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    song_is_play = False
                    songs_list[song_counter].stop()
                #старт секрет кнопка
                if event.key == pygame.K_q:
                    song_is_play = True
                    songs_list[song_counter].play()
                #смена песен вперед
                if event.key == pygame.K_d:
                    songs_list[song_counter].stop()
                    song_counter += 1
                    
                    #счетчик песен
                    song_counter %= amount_of_songs
                    
                    songs_list[song_counter].play()
                #смена песен назад
                if event.key == pygame.K_a:
                    songs_list[song_counter].stop()
                    
                    if song_counter == 0:
                        song_counter = 4
                    else:
                        song_counter -= 1
                    #тоже чтобы не вышла за грань 
                    song_counter %= amount_of_songs
                    
                    songs_list[song_counter].play()
                #остановить или начать песню 
                if event.key == pygame.K_SPACE:
                    if stop_sound:
                        songs_list[song_counter].stop()
                        stop_sound = False
                    else:
                        songs_list[song_counter].play()
                        stop_sound = True
                                       
main()