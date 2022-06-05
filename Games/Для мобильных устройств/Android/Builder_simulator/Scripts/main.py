import pygame
from random import randrange as rnd
pygame.font.init()

WIDTH, HEIGHT = 1500, 1000
fps = 60

# block settings
hero_w = 50
hero_h = 50
hero_speed = 10
hero = pygame.Rect(WIDTH // 2 - hero_w // 2, HEIGHT -270, hero_w, hero_h)

enemy1_w = 50
enemy1_h = 50
enemy1_speed = 1
enemy1 = pygame.Rect(WIDTH // 3 - hero_w // 2, HEIGHT -270, hero_w, hero_h)

blocks_num_horisontal =38
blocks_num_vertical = 1

# blocks settings
block_list = [pygame.Rect(0 + 50* i, (1080-300) + 80 * j, 50, 50) for i in range(blocks_num_horisontal) for j in range(blocks_num_vertical)]
color_list = [(0,100,34) for i in range(blocks_num_horisontal) for j in range(blocks_num_vertical)]

block_list1 = [pygame.Rect(0 + 50 * i, (1080-250)+ 80 * j, 50, 50) for i in range(blocks_num_horisontal) for j in range(blocks_num_vertical)]
color_list1 = [(142,86,0) for i in range(blocks_num_horisontal) for j in range(blocks_num_vertical)]

block_list2 = [pygame.Rect(0 + 50 * i, (1080-200) + 80 * j, 50, 50) for i in range(blocks_num_horisontal) for j in range(blocks_num_vertical)]
color_list2 = [(133,133,133) for i in range(blocks_num_horisontal) for j in range(blocks_num_vertical)]

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
bgmusic = pygame.mixer.music.load('music/bensound-birthofahero.mp3')

music_volumes = [0,1]

music_volume = music_volumes[0]
pygame.mixer.music.set_volume(music_volume)
pygame.mixer.music.play(-1)
sound1 = pygame.mixer.Sound('select1.wav')

# backgrund image
img = pygame.image.load('1.jpg').convert()

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    sc.blit(img, (0, 0))

    # drawing world
    [pygame.draw.rect(sc, color_list[color], block) for color, block in enumerate(block_list)]
    [pygame.draw.rect(sc, color_list1[color], block) for color, block in enumerate(block_list1)]
    [pygame.draw.rect(sc, color_list2[color], block) for color, block in enumerate(block_list2)]
    pygame.draw.rect(sc, pygame.Color(255,255,255), hero)
    pygame.draw.rect(sc, pygame.Color(255,0,0), enemy1)

    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1 and hero_speed >= 0:
            hero.x -= 10
        if event.button == 3 and hero_speed >= 0:
            hero.x += 10

    if enemy1.x <= hero.x:
        enemy1.x += enemy1_speed

    if enemy1.x >= hero.x:
        enemy1.x -= enemy1_speed

    # control
    key = pygame.key.get_pressed()
    if key[pygame.K_a] and hero.left > 0:
        hero.left -= hero_speed
    if key[pygame.K_d] and hero.right < WIDTH:
        hero.right += hero_speed

    if key[pygame.K_q]:
        quit()

    if key [pygame.K_y]:
        music_volume = music_volumes[0]
        pygame.mixer.music.set_volume(music_volume)
    if key [pygame.K_u]:
        music_volume = music_volumes[1]
        pygame.mixer.music.set_volume(music_volume)

    # update screen
    pygame.display.flip()
    clock.tick(fps)
