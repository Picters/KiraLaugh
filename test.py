import pygame
import sys
import random

# ������������� Pygame
pygame.init()
pygame.mixer.init()

# ��������� ������ � ����
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # ������������� ����� � ����������� �������
pygame.display.set_caption("PicProjectV5.Beta")
clock = pygame.time.Clock()

# �������� ��������
bg_music = './assets/sfx/fun.mp3'
kira_image = pygame.image.load('./assets/characters/kira.png')
kira_rect = kira_image.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
pygame.mixer.music.load(bg_music)
pygame.mixer.music.play(-1)

# �����
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
current_color = random.choice(colors)

# ������
font = pygame.font.SysFont("Arial", 50)
title_font = pygame.font.SysFont("Arial", 70)

# ������
title_text = title_font.render("PicProjectV5.Beta", True, (255, 255, 255))
play_text = font.render("������", True, (255, 255, 255))
exit_text = font.render("�����", True, (255, 255, 255))

# ������
play_button = play_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 100))
exit_button = exit_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 200))

# ��������� �������� � �������� ����
kira_speed = [5, 5]
rotation_angle = 0

def change_background():
    global current_color
    current_color = random.choice(colors)

# �������� ���� ����
while True:
    screen.fill(current_color)

    # �������� ���
    if pygame.time.get_ticks() % 500 == 0:
        change_background()

    # �������� ����
    kira_rect = kira_rect.move(kira_speed)
    if kira_rect.left < 0 or kira_rect.right > screen.get_width():
        kira_speed[0] = -kira_speed[0]
    if kira_rect.top < 0 or kira_rect.bottom > screen.get_height():
        kira_speed[1] = -kira_speed[1]
    
    # �������� ����
    rotation_angle += 5
    rotated_kira = pygame.transform.rotate(kira_image, rotation_angle)
    rotated_rect = rotated_kira.get_rect(center=kira_rect.center)
    screen.blit(rotated_kira, rotated_rect)

    # ����������� ������
    screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 50))
    screen.blit(play_text, play_button)
    screen.blit(exit_text, exit_button)

    # ��������� �������
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.collidepoint(event.pos):
                print("���� ����������!")  # �������� ��� ������� ���� �����
            elif exit_button.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

    pygame.display.flip()
    clock.tick(60)
