import time
import pygame
import sys

pygame.init()

WIDTH = 1000
HEIGHT = 600

background = pygame.image.load('image.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Escape room #2")

font = pygame.font.Font(None, 36)

