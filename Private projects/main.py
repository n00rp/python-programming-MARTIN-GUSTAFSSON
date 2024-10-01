import pygame
from os.path import join
from random import randint
#general setup
pygame.init()
title = pygame.display.set_caption("My First Game")
window_width, window_height = 1280,720
display_surface = pygame.display.set_mode((window_width, window_height))

running = True

#creat a sruface
surface = pygame.Surface((100,200))
surface.fill("orange")
x = 100

#imports
player_surface = pygame.image.load("Data/space shooter/images/player.png").convert_alpha()
star_surface = pygame.image.load(join("Data","space shooter","images","star.png")).convert_alpha()

meteor_surface = pygame.image.load(join("Data","space shooter","images","meteor.png")).convert_alpha()
meteor_rect = meteor_surface.get_frect(center = (window_width/2,window_height/2))


player_rect = player_surface.get_frect(center = (window_width/2,window_height/2))

star_positions = [(randint(0,window_width),randint(0,window_height)) for i in range(20)]
while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #fill the game with red color
    display_surface.fill(("darkgrey"))
    for pos in star_positions:
        display_surface.blit(star_surface, pos)
    if player_rect.right < window_width:
        player_rect.left += 0.2
    
    display_surface.blit(player_surface, player_rect)
    pygame.display.update()
#draw game           
pygame.quit()    


#56:07 på youtube