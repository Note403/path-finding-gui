import sys

import pygame
from entities.field import Field

pygame.init()
pygame.display.set_caption("Path Finding")
pygame.key.set_repeat(True)


class Game:
    def __init__(self):
        self.size = width, height = 720, 420
        self.display = pygame.display.set_mode(self.size)
        self.obstacles = []
        self.field = Field(height, width, 30, 30)
        self.clock = pygame.time.Clock()

    def game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    keys_pressed = pygame.key.get_pressed()
                    if keys_pressed[pygame.K_r]:
                        self.field.reset()

                    if keys_pressed[pygame.K_k]:
                        if self.field.ki.rect.width == 0:
                            self.field.spawn_ki()

                    if keys_pressed[pygame.K_RETURN]:
                        self.field.ki.find_path(self.field.rects_outline, self.field.goal)

                if event.type == pygame.MOUSEBUTTONUP and self.field.drag_ki:
                    self.field.place_ki()
                    self.field.drag_ki = False

                if pygame.mouse.get_pressed()[0]:
                    if self.field.ki.rect.collidepoint(pygame.mouse.get_pos()) or self.field.drag_ki:
                        self.field.move_ki()

                        if not self.field.drag_ki:
                            self.field.drag_ki = True
                    else:
                        self.field.color_rect()

                if pygame.mouse.get_pressed()[1]:
                    self.field.set_goal()

                if pygame.mouse.get_pressed()[2]:
                    self.field.remove_color_rect()

            self.display.fill((0, 0, 0))

            for rect in self.field.rects_outline:
                pygame.draw.rect(
                    self.display,
                    (50, 50, 50),
                    rect,
                    1,
                )

            for rect in self.field.rects_filled:
                pygame.draw.rect(
                    self.display,
                    (20, 200, 255),
                    rect
                )

            pygame.draw.rect(self.display, (220, 50, 50), self.field.goal)

            pygame.draw.rect(
                self.display,
                self.field.ki.color,
                self.field.ki.rect
            )

            pygame.display.flip()
            self.clock.tick(60)


game = Game()
game.game()
