import os
import random
import sys
import time

import pygame
from pygame import mixer

import asyncio

pygame.init()
mixer.init()
x = 0


def quitmain():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False


pressed = False
directory = sys.path[0]
hitsound = os.path.join(directory, "../Assets/hit.mp3")
cur = os.path.join(directory, "../Assets/cursor.png")
target = os.path.join(directory, "../Assets/obj.png")
backgroud = os.path.join(directory, "../Assets/spawn area.png")
quitbutton = os.path.join(directory, "../Assets/quit.png")

hit = pygame.mixer.Sound(hitsound)

cursor = pygame.image.load(cur)

click = False
target = pygame.image.load(target)
targetX = random.randint(250, 1616 - 10)
targetY = random.randint(74, 1080 - 74)


def player(x, y):
    screen.blit(target, (x, y))


score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


textX = 10
testY = 10

pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Aim Trainer")
running = True
color = (255, 0, 0)
Rectplace = pygame.image.load(backgroud)
quitbutton = pygame.image.load(quitbutton)
quitbox = pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(220, 100, 220, 100))


def quit():
    global pressed
    global running
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z or event.key == pygame.K_x:
                if hitbox.collidepoint(pos):
                    pressed = True
    if quitbox.collidepoint(pos) and pressed == True:
        pressed = False
        running = False

async def randomise_target():
    global targetX
    global targetY
    targetX = random.randint(250, 1616 - 10)
    targetY = random.randint(10, 1080 - 74)

async def play_hitsound():
    hit.play()
    time.sleep(0.05)
    hit.stop()



async def objects():
    global hitbox
    screen.blit(Rectplace, (240, 0))
    show_score(textX, testY)
    hitbox = pygame.draw.circle(screen, (0, 0, 0), (targetX + 32, targetY + 32), 32, 1)
    screen.blit(cursor, (pygame.mouse.get_pos()))

async def target_click(pos):
    global click
    global targetX
    global targetY
    global score_value
    global hitbox
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z or event.key == pygame.K_x:
                if hitbox.collidepoint(pos):
                    click = True
        elif hitbox.collidepoint(pos) and click == True:
            click = False
            score_value = score_value + 1
            await randomise_target()
            await play_hitsound()
async def init_display():
    screen.fill((0, 0, 0))
    screen.blit(quitbutton, (1699, 0))

#clock = pygame.time.Clock()
while running:
    asyncio.run(init_display())
    asyncio.run(objects())
    asyncio.run(target_click(pygame.mouse.get_pos()))
    player(targetX, targetY)
    pygame.display.flip()
