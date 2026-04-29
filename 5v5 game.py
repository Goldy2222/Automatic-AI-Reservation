import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()
pygame.mixer.init()

pygame.display.set_caption("Main Menu")

WIDTH, HEIGHT = 1000, 650
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))


def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image


def draw_game(WIN, bg_image, terrain):
    WIN.blit(bg_image, (0, 0))

    tile_width = terrain.get_width()
    for x in range(0, WIDTH, tile_width):
        WIN.blit(terrain, (x, HEIGHT - terrain.get_height()))

    pygame.display.update()


def draw(WIN, background, bg_image, mute_icon, mute_btn, muted, play_img, play_btn, exit_img, exit_btn, mouse_pos):
    for tile in background:
        WIN.blit(bg_image, tile)

    if muted:
        dark = mute_icon.copy()
        dark.set_alpha(80)
        WIN.blit(dark, mute_btn)
    else:
        WIN.blit(mute_icon, mute_btn)

    if play_btn.collidepoint(mouse_pos):
        dark_play = play_img.copy()
        dark_play.set_alpha(150)
        WIN.blit(dark_play, play_btn)
    else:
        WIN.blit(play_img, play_btn)

    if exit_btn.collidepoint(mouse_pos):
        dark_play = exit_img.copy()
        dark_play.set_alpha(150)
        WIN.blit(dark_play, exit_btn)
    else:
        WIN.blit(exit_img, exit_btn)

    pygame.display.update()


def game(WIN):
    clock = pygame.time.Clock()

    bg_image = pygame.image.load(
        join("assets", "Background", "bg.jpg")).convert()
    bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

    terrain = pygame.image.load(
        join("assets", "Terrain", "Grass.jpg")).convert()
    terrain = pygame.transform.scale(
        terrain, (80, 80))

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        draw_game(WIN, bg_image, terrain)


def main(WIN):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Yellow.jpg")

    pygame.mixer.music.load(join("assets", "Music", "bgm.mp3"))
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=1)

    mute_icon = pygame.image.load(
        join("assets", "Button", "Volume.jpg")).convert()
    mute_icon = pygame.transform.scale(mute_icon, (40, 40))
    mute_btn = mute_icon.get_rect(topleft=(20, 20))
    muted = False

    play_img = pygame.image.load(
        join("assets", "Button", "Start.jpg")).convert()
    play_img = pygame.transform.scale(play_img, (200, 80))
    play_btn = play_img.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60))

    exit_img = pygame.image.load(
        join("assets", "Button", "Exit.jpg")).convert()
    exit_img = pygame.transform.scale(exit_img, (200, 80))
    exit_btn = exit_img.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mute_btn.collidepoint(event.pos):
                    muted = not muted
                    pygame.mixer.music.set_volume(0 if muted else 0.5)

                if play_btn.collidepoint(event.pos):
                    game(WIN)

                if exit_btn.collidepoint(event.pos):
                    run = False

        mouse_pos = pygame.mouse.get_pos()

        draw(WIN, background, bg_image, mute_icon, mute_btn,
             muted, play_img, play_btn, exit_img, exit_btn, mouse_pos)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main(WIN)
