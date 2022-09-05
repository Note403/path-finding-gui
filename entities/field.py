import pygame

from entities.ki import KI


class Field:
    def __init__(self, f_height, f_width, r_height, r_width):
        self.f_height = f_height
        self.f_width = f_width
        self.r_height = r_height
        self.r_width = r_width
        self.furthest_x = 0
        self.furthest_y = 0
        self.goal = pygame.Rect(0, 0, 0, 0)

        self.rects_outline = []
        self.rects_filled = []

        self.ki = KI(self.r_width, self.f_width, self.f_height)

        self.drag_ki = False

        while self.furthest_y < self.f_height:
            while self.furthest_x < self.f_width:
                self.rects_outline.append(pygame.Rect(
                    self.furthest_x,
                    self.furthest_y,
                    self.r_width,
                    self.r_height
                ))

                self.furthest_x += self.r_width

            self.furthest_y += self.r_height
            self.furthest_x = 0

    def color_rect(self):
        mouse_pos = pygame.mouse.get_pos()

        for rect in self.rects_outline:
            if rect.collidepoint(mouse_pos):
                self.rects_outline.remove(rect)
                self.rects_filled.append(rect)
                return

    def remove_color_rect(self):
        mouse_pos = pygame.mouse.get_pos()

        for rect in self.rects_filled:
            if rect.collidepoint(mouse_pos):
                self.rects_filled.remove(rect)
                self.rects_outline.append(rect)

    def set_goal(self):
        mouse_pos = pygame.mouse.get_pos()

        if not self.is_free(mouse_pos):
            return False

        if self.goal.width != 0:
            self.rects_outline.append(self.goal)
            self.goal = pygame.Rect(0, 0, 0, 0)

        for rect in self.rects_outline:
            if rect.collidepoint(mouse_pos):
                self.rects_outline.remove(rect)
                self.goal = rect

    def spawn_ki(self):
        ki_rect = None

        for rect in self.rects_outline:
            if ki_rect is None:
                ki_rect = rect
                continue

            if rect.x < ki_rect.x and rect.y < ki_rect.y:
                ki_rect = rect

        self.ki.generate(ki_rect)
        self.rects_outline.remove(ki_rect)

    def is_free(self, mouse_pos):
        if self.goal.collidepoint(mouse_pos):
            return False

        for rect in self.rects_filled:
            if rect.collidepoint(mouse_pos):
                return False

        return True

    def reset(self):
        self.rects_outline.append(self.goal)
        self.goal = pygame.Rect(0, 0, 0, 0)

        self.rects_outline.append(self.ki.rect)
        self.ki.rect = pygame.Rect(0, 0, 0, 0)

        for rect in self.rects_filled:
            self.rects_filled.remove(rect)
            self.rects_outline.append(rect)

    def move_ki(self):
        mouse_pos = pygame.mouse.get_pos()

        if not self.drag_ki:
            print("append old ki-rect")
            print(self.ki.rect)
            self.rects_outline.append(self.ki.rect)

        self.ki.rect.x = mouse_pos[0] - (self.ki.rect.width / 2)
        self.ki.rect.y = mouse_pos[1] - (self.ki.rect.height / 2)

    def place_ki(self):
        mouse_pos = pygame.mouse.get_pos()

        for rect in self.rects_outline:
            if rect.collidepoint(mouse_pos):
                self.rects_outline.remove(rect)
                self.ki.rect = rect
                return
