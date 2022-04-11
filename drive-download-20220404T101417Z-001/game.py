import pygame, sys
from random import randint
pygame.init()
pygame.mixer.init()

ekraan = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Mäng")

laev = pygame.image.load("spaceship.png")
täht = pygame.image.load("star.png")
alien = pygame.image.load("alien.png")
süda = pygame.image.load("heart.png")
taust = pygame.image.load('background3.jpg')

laev = pygame.transform.scale(laev, (200, 100))
täht = pygame.transform.scale(täht, (50, 50))
alien = pygame.transform.scale(alien, (100, 100))
süda = pygame.transform.scale(süda, (75, 75))
taust = pygame.transform.scale(taust, (1092,600))

heli = pygame.mixer.Sound('punkt.wav')
hit = pygame.mixer.Sound('hit.wav')
startsound = pygame.mixer.Sound('startsound.wav')
pygame.mixer.music.load('taust.mp3')
pygame.mixer.music.set_volume(0.3)

teksti_font = pygame.font.Font('font.ttf', 45)
font = pygame.font.Font('font.ttf', 100)

laev_x = 200
laev_y = 200
täht_x = 800
täht_y = 30
alien_x = 800
alien_y = 400
süda_x = 25
süda_y = 25
täht_samm = randint(1,3)
alien_samm = randint(1,3)
samm = 12
elud = 5
punktid = 0
streak = 0
max_streak = 0
started = False

running = True
pygame.key.set_repeat(1,10)
while running:
    
    if not started:
        ekraan.fill([0, 0, 0])
        tekst_game_name = font.render("Spaceship", 1, [255, 255, 0])
        tekst_game_start = teksti_font.render("> Start Game", 1, [255, 255, 255])
        ekraan.blit(tekst_game_name, [140,120])
        ekraan.blit(tekst_game_start, [140,240])
           
    else:
        ekraan.blit(taust, [0,0])
        
        täht_x -= täht_samm
        alien_x -= alien_samm
        pygame.time.delay(2)

        tekst_streak = teksti_font.render("Streak: " + str(streak), 1, [255, 255, 255])
        tekst_pildina = teksti_font.render("Score: " + str(punktid), 1, [255, 255, 255])
    
        ekraan.blit(tekst_streak, [40, 150])
        ekraan.blit(tekst_pildina, [40, 100])
        ekraan.blit(täht, (täht_x, täht_y))
        
        ekraan.blit(alien, (alien_x,alien_y))
        ekraan.blit(laev, (laev_x,laev_y))
        
        süda_x = 25
        for i in range(0, elud):
            
            ekraan.blit(süda, (süda_x,süda_y))
            süda_x += 75
    
    
    if täht_x < 0:
        täht_x = 800
        täht_y = randint(0,550)
        täht_samm = randint(1,4)
        streak = 0
        
    if alien_x < 0:
        alien_x = 800
        alien_y = randint(0,600)
        alien_samm = randint(1,3)
      
    if laev_x > täht_x - 200 and laev_x < täht_x + 50 and laev_y > täht_y - 75 and laev_y < täht_y + 50:
        täht_x = 800
        täht_y = randint(0,550)
        täht_samm = randint(1,4)
        punktid += 1
        streak = streak + 1
        heli.play()
        if streak > max_streak:
            max_streak = streak
        
    if laev_x > alien_x - 200 and laev_x < alien_x + 75 and laev_y > alien_y - 75 and laev_y < alien_y + 75:
        alien_x = 800
        alien_y = randint(0,600)
        elud -= 1
        hit.play()
    if elud <= 0:
        täht_x = 800
        täht_y = 600
        laev_x = 10
        laev_y = 300
        täht_samm = 0
        alien_samm = 0
        ekraan.fill([0,0,0])
        
        tekst_game_over = font.render("GAME OVER!", 1, [255, 0, 0])
        tekst_end_score = teksti_font.render("Score: " + str(punktid), 1, [255, 255, 255])
        tekst_max_streak = teksti_font.render("Max streak: " + str(max_streak), 1, [255, 255, 255])
        tekst_quit = teksti_font.render("> Quit game",1 , [255,255,255])
        tekst_restart = teksti_font.render("> Try again",1 , [255,255,255])
        
        ekraan.blit(tekst_game_over, [130, 150])
        ekraan.blit(tekst_end_score, [135, 250])
        ekraan.blit(tekst_max_streak, [135, 300])
        ekraan.blit(tekst_quit, [135, 400])
        ekraan.blit(tekst_restart, [135, 350])
        
    pygame.display.flip()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                if laev_y <= -100:
                    laev_y = 600 
                laev_y = laev_y - samm
            elif i.key == pygame.K_DOWN:
                if laev_y >= 600:
                    laev_y = -100
                laev_y = laev_y + samm
            elif i.key == pygame.K_LEFT:
                if laev_x <= -200:
                    laev_x = 800
                laev_x = laev_x - samm
            elif i.key == pygame.K_RIGHT:
                if laev_x >= 800:
                    laev_x = -200
                laev_x = laev_x + samm
        elif i.type == pygame.MOUSEBUTTONDOWN:
            hiir_x, hiir_y = i.pos
            # start game
            if hiir_x > 180 and hiir_x < 500 and hiir_y > 250 and hiir_y < 300:
                started = True
                pygame.mixer.music.play()
                startsound.play()
            # quit game
            if hiir_x > 135 and hiir_x < 435 and hiir_y > 400 and hiir_y < 450 and started:
                running = False
            # try again
            if hiir_x > 135 and hiir_x < 435 and hiir_y > 350 and hiir_y < 400 and started:
                elud = 5
                punktid = 0
                max_streak = 0
                streak = 0
                täht_samm = randint(1,4)
                alien_samm = 1
                pygame.mixer.music.play()
                startsound.play()
pygame.quit()
