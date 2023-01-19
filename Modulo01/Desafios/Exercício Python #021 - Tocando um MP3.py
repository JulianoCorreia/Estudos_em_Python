'''
Faça um programa em Python que abra e reproduza o áudio
de um arquivo MP3.
'''

print('=====   DESAFIO 021   =====')

import pygame

# Iniciando o mixer
pygame.mixer.init()

# Iniciando o pygame
pygame.init()

pygame.mixer.music.load('codfish.mp3')
pygame.mixer.music.play()
pygame.event.wait()
