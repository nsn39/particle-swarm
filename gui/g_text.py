from gui.g_common import *
import pygame


class Text_G:
    def __init__(self, text: str, pos: tuple, size: int, color: tuple, pos_wrt_center: bool) -> None:
        self.font = pygame.font.Font(FONT_FILE, size)
        self.color = color

        self.text = text
        self.text_surface = self.font.render(self.text, True, self.color)
        if pos_wrt_center:
            self.pos= self.text_surface.get_rect(center=pos)
        else:
            self.pos = pos

    def draw_text(self, surface) -> None:
        surface.blit(self.text_surface, self.pos)
    
    def draw_updated_text(self, surface, text: str) -> None:
        self.text = text
        self.text_surface = self.font.render(self.text, True, self.color)
        surface.blit(self.text_surface, self.pos)

