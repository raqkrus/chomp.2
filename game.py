import pygame
#pygame setup
pygame.init()
#set resolution of our game window
WIDTH = 1080
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))


#load our players (fish)
puffer_fish = pygame.image.load('fish/puffer_fish.png')
water_tile = pygame.image.load('fish/fishTile_089.png')
sand_top_tile = pygame.image.load('fish/fishTile_021.png')
tile_width = water_tile.get_width()
tile_height = water_tile.get_height()
sand_tile = pygame.image.load('fish/fishTile_126.png')

#make background
background = pygame.Surface((WIDTH, HEIGHT))

#draw water tiles
for x in range(0,WIDTH,tile_width):
    for y in range(0,HEIGHT,tile_height):
        background.blit(water_tile, (x,y))

#draw sand tiles
for x in range(0,WIDTH,tile_width):
    for y in range(0,HEIGHT,tile_height):
        background.blit(sand_top_tile, (x,HEIGHT-2*tile_height)

running = True

while running:
    #poll for events
    #pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #add a fish and blit it to the screen
    screen.blit(puffer_fish,(WIDTH/2, HEIGHT/2))

    #render your game here

    #flip(_) the display to put your work on the screen
    pygame.display.flip()

pygame.quit()




