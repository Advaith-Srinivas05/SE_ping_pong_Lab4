import pygame
import random

# Initialize mixer here (safe to do once)
pygame.mixer.init()

class Ball:
    def __init__(self, x, y, width, height, screen_width, screen_height):
        self.original_x = x
        self.original_y = y
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.velocity_x = random.choice([-5, 5])
        self.velocity_y = random.choice([-3, 3])

        # Load sounds once
        self.sound_paddle = pygame.mixer.Sound("sounds/paddle_hit.wav")
        self.sound_wall = pygame.mixer.Sound("sounds/wall_bounce.wav")
        self.sound_score = pygame.mixer.Sound("sounds/score.wav")

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

        if self.y <= 0 or self.y + self.height >= self.screen_height:
            self.velocity_y *= -1
            self.sound_wall.play()

    def check_collision(self, player, ai):
        ball_rect = self.rect()
        player_rect = player.rect()
        ai_rect = ai.rect()

        # Collision with player paddle
        if ball_rect.colliderect(player_rect) and self.velocity_x < 0:
            self.velocity_x *= -1
            # Push the ball outside the paddle to prevent sticking
            self.x = player_rect.right
            self.sound_paddle.play()

        # Collision with AI paddle
        elif ball_rect.colliderect(ai_rect) and self.velocity_x > 0:
            self.velocity_x *= -1
            self.x = ai_rect.left - self.width
            self.sound_paddle.play()

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.velocity_x *= -1
        self.velocity_y = random.choice([-3, 3])
        self.sound_score.play()

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
