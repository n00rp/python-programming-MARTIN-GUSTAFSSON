import pygame
from os.path import join
from random import randint, uniform

#Classes

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join("Data","space shooter","images","player.png")).convert_alpha()
        self.rect = self.image.get_frect(center = (window_width / 2,window_height / 2))
        self.direction = pygame.math.Vector2()
        self.speed = 300

        #Coldown section
        self.can_shoot = True
        self.shoot_time = 0
        self.cooldown_duration = 400

        #Mask
        mask = pygame.mask.from_surface(self.image)
        

    
    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True

    def update(self, dt):
        keys =pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN] - keys[pygame.K_UP])
        self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

        recent_keys = pygame.key.get_just_pressed() 
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            Laser(laser_surface, self.rect.midtop, (all_sprites, laser_sprites))
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()
            laser_sound.play()

        self.laser_timer()
class Star(pygame.sprite.Sprite):
    def __init__(self,groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = (randint(0,window_width),randint(0,window_height)))
class Laser(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midtop = pos)
        

    def update(self,dt):
        self.rect.centery -= 400 * dt
        if self.rect.bottom < 0:
            self.kill()
class Meteor(pygame.sprite.Sprite):
    def __init__(self,surf, pos, groups):
        super().__init__(groups)
        self.original_surface = surf
        self.image = surf
        self.rect = surf.get_frect(center = pos)
        self.start_time = pygame.time.get_ticks()
        self.lifetime = 3000
        self.direction = pygame.Vector2(uniform(-0.5, 0.5),1)
        self.speed = randint(400, 500)
        self.rotation_speed = randint(40, 90)
        self.rotation = 0

    def update(self,dt):
        self.rect.center += self.direction * self.speed * dt
        if pygame.time.get_ticks() - self.start_time >= self.lifetime:
            self.kill()
        self.rotation += self.rotation_speed * dt
        self.image = pygame.transform.rotozoom(self.original_surface, self.rotation, 1)
        self.rect = self.image.get_frect(center = self.rect.center)
class AnimetedExplosion(pygame.sprite.Sprite):
    def __init__(self, frames, pos, groups):
        super().__init__(groups)
        self.frames = frames
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_frect(center = pos)
        explosion_sound
    def update(self, dt):
        self.frame_index += 20 * dt
        if self.frame_index < len(self.frames):
            self.image = self.frames[int(self.frame_index)]
        else:
            self.kill()

def collisions():
    global running

    collisions_sprites = pygame.sprite.spritecollide(player, meteor_sprites, True, pygame.sprite.collide_mask)
    if collisions_sprites:
        running = False
    
    for laser in laser_sprites:
        collided_sprites = pygame.sprite.spritecollide(laser, meteor_sprites, True)
        if collided_sprites:
            laser.kill()
            AnimetedExplosion(explosion_frame, laser.rect.midtop, all_sprites)
            
def displaty_score():
    current_time = pygame.time.get_ticks() // 100
    text_surface = font.render(str(current_time), True, (230,230,230))
    text_rect = text_surface.get_frect(midbottom = (window_width / 2, window_height - 50))
    display_surface.blit(text_surface, text_rect)
    pygame.draw.rect(display_surface, (230,230,230), text_rect.inflate(20,10).move(0,-8), 5, 10)
#General Setup
pygame.init()
title = pygame.display.set_caption("My First Game")
window_width, window_height = 1280,720
display_surface = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
running = True

#Imports

meteor_surface = pygame.image.load(join("Data","space shooter","images","meteor.png")).convert_alpha()
star_surf = pygame.image.load(join("Data","space shooter","images","star.png")).convert_alpha()
laser_surface = pygame.image.load(join("Data","space shooter","images","laser.png")).convert_alpha()
font = pygame.font.Font(join("Data","space shooter","images","Oxanium-Bold.ttf"), 50)
explosion_frame = [pygame.image.load(join("Data", "space shooter", "images", "explosion",f"{i}.png")).convert_alpha() for i in range(21)]

#Sounds
laser_sound = pygame.mixer.Sound(join("Data","space shooter","audio","laser.wav"))
laser_sound.set_volume(0.05)
explosion_sound = pygame.mixer.Sound(join("Data","space shooter","audio","explosion.wav"))
game_music = pygame.mixer.Sound(join("Data","space shooter","audio","game_music.wav"))
game_music.set_volume(0.05)
game_music.play(-1)


#All Sprites 
all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()   
for i in range(20):
    star = Star(all_sprites,star_surf)
player = Player(all_sprites)


#custom events ---> Meteor event
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)


while running:
    dt =clock.tick() / 1000
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            x, y = randint(0,window_width), randint(-200,-100)
            Meteor(meteor_surface, (x, y), (all_sprites, meteor_sprites))
    

    #update
    all_sprites.update(dt)
    collisions()

    
    #draw game
    display_surface.fill("#3a2e3f")
    displaty_score()
    all_sprites.draw(display_surface)

    
    pygame.display.update()        
pygame.quit()    


