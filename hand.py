import pygame
import helper.image as image
from helper.settings import *
from helper.hand_tracking import HandTracking
import cv2

class Hand:
    def __init__(self):
        self.orig_image = image.load("Assets/hand.png", size=(HAND_SIZE, HAND_SIZE))
        self.image = self.orig_image.copy()
        self.image_smaller = image.load("Assets/hand.png", size=(HAND_SIZE - 50, HAND_SIZE - 50))
        self.rect = pygame.Rect(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, HAND_HITBOX_SIZE[0], HAND_HITBOX_SIZE[1])
        self.left_click = False

    def follow_mouse(self):
        self.rect.center = pygame.mouse.get_pos()

    def follow_mediapipe_hand(self, x, y):
        self.rect.center = (x, y)

    def draw_hitbox(self, surface):
        pygame.draw.rect(surface, (200, 60, 0), self.rect)

    def draw(self, surface):
        image.draw(surface, self.image, self.rect.center, pos_mode="center")
        if DRAW_HITBOX:
            self.draw_hitbox(surface)

    def on_insect(self, insects):
        return [insect for insect in insects if self.rect.colliderect(insect.rect)]
    
    def kill_insects(self, insects, score):
        if self.left_click: # if left click
            for insect in self.on_insect(insects):
                insect_score = insect.kill(insects)
                score += insect_score
        else:
            self.left_click = False
        return score
