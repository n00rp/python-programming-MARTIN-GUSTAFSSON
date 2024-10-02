import pygame
from os.path import join
from random import randint
#General Setup
pygame.init()
title = pygame.display.set_caption("My First Game")
window_width, window_height = 1280,720
display_surface = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

running = True

#creat a sruface
surface = pygame.Surface((100,200))
surface.fill("orange")
x = 100

#imports
player_surface = pygame.image.load("Data/space shooter/images/player.png").convert_alpha()
player_rect = player_surface.get_frect(center = (window_width/2,window_height/2))   
player_direction = pygame.math.Vector2(1, 0)
player_speed = 10

star_surface = pygame.image.load(join("Data","space shooter","images","star.png")).convert_alpha()
star_positions = [(randint(0,window_width),randint(0,window_height)) for i in range(20)]

meteor_surface = pygame.image.load(join("Data","space shooter","images","meteor.png")).convert_alpha()
meteor_rect = meteor_surface.get_frect(center = (window_width/2,window_height/2))

laser_surface = pygame.image.load(join("Data","space shooter","images","laser.png")).convert_alpha()
laser_rect = laser_surface.get_frect(bottomleft = (20,window_height - 20))

player_rect = player_surface.get_frect(center = (window_width/2,window_height/2))



while running:
    clock.tick(20)
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #fill the game with red color
    display_surface.fill(("darkgrey"))
    for pos in star_positions:
        display_surface.blit(star_surface, pos)
    
    display_surface.blit(meteor_surface, meteor_rect)
    display_surface.blit(laser_surface, laser_rect)

    #player movement   
    player_rect.center += player_direction * player_speed

    
    


    display_surface.blit(player_surface, player_rect)
    
    pygame.display.update()
#draw game           
pygame.quit()    


#56:07 på youtube