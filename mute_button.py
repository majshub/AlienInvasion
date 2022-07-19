import pygame


class MuteButton:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.sb = ai_game.sb
        self.prep_mute_button()

    def prep_mute_button(self):
        self.image = pygame.image.load('images/unmute.png')
        self.rect = self.image.get_rect()
        self.rect.top = self.sb.level_rect.bottom + 10
        self.rect.right = self.sb.level_rect.right

    def mute_blit(self):
        if self.settings.is_mute > 0:
            self.image = pygame.image.load('images/mute.png')
        elif self.settings.is_mute < 0:
            self.image = pygame.image.load('images/unmute.png')

        self.screen.blit(self.image, self.rect)

