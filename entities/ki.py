import pygame


class KI:
    def __init__(self, r_width, f_width, f_height):
        self.color = (20, 255, 20)
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.step = r_width
        self.f_height = f_height
        self.f_width = f_width
        self.tiles_value = []

    def generate(self, rect):
        self.rect = rect
