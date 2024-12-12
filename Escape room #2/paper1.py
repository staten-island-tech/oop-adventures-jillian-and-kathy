import time
import pygame
import sys

screen_width = 1920
screen_height = 1017

background_image = pygame.image.load('image.jpg')  # Add your own background image
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))