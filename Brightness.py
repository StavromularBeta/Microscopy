#!/usr/bin/env python

import pygame

pygame.init()
w = 500
h = 500
size = (w, h)
screen = pygame.display.set_mode(size)
pygame.display.flip()


TestDogPic = pygame.image.load('TestDogPic.jpg')
TestDogPic = pygame.transform.scale(TestDogPic, (500, 500))
screen.blit(TestDogPic, (0, 0))
pygame.display.flip()

running = True
y_value = 0
x_value = range(0, 500)


def dimmer_switch(x, y):
    for pixel in x:
        if pixel < 500:
            pixel_color = TestDogPic.get_at((pixel, y))
            dim_pixel_color = pixel_color // pygame.Color(3, 3, 3, 3)
            TestDogPic.set_at((pixel, y), dim_pixel_color)

while y_value < 500:
    dimmer_switch(x_value, y_value)
    y_value = y_value + 1


screen.blit(TestDogPic, (0, 0))
pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

