"""
renderer: all pygame drawing lives here, kept separate from game logic.
"""

import pygame

WIDTH, HEIGHT = 700, 500
WINDOW_SIZE = (WIDTH, HEIGHT)

COLOR_BG = (200, 230, 245)
COLOR_TEXT = (30, 30, 30)


def draw_scene(surface, balloons):
    surface.fill(COLOR_BG)
    for b in balloons:
        pygame.draw.circle(surface, b.color, (int(b.x), int(b.y)), b.radius)
        pygame.draw.line(
            surface,
            (120, 120, 120),
            (b.x, b.y + b.radius),
            (b.x, b.y + b.radius + 12),
            2,
        )


def draw_text(surface, font, text, pos, color=COLOR_TEXT):
    surface.blit(font.render(text, True, color), pos)


def draw_banner(surface, font, text):
    surf = font.render(text, True, (180, 40, 40))
    rect = surf.get_rect(center=(surface.get_width() // 2, surface.get_height() // 2))
    surface.blit(surf, rect)


def draw_game_over(surface, font, score):
    draw_banner(surface, font, "ROUND OVER")

    score_surf = font.render(f"Final Score: {score}", True, COLOR_TEXT)
    score_rect = score_surf.get_rect(
        center=(surface.get_width() // 2, surface.get_height() // 2 + 40)
    )
    surface.blit(score_surf, score_rect)

    restart_surf = font.render("Press R to start a new round", True, COLOR_TEXT)
    restart_rect = restart_surf.get_rect(
        center=(surface.get_width() // 2, surface.get_height() // 2 + 75)
    )
    surface.blit(restart_surf, restart_rect)
