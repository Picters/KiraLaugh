import pygame
import random
import sys
import keyboard
import time
from pydub import AudioSegment

# Инициализация Pygame
pygame.init()
pygame.mixer.init()

# Настройки окна
screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Смешной Кирилл Тихомиров")

# Загрузка изображения Кирилла
kira_image = pygame.image.load('./assets/character/kira.png')
kira_image = pygame.transform.scale(kira_image, (100, 100))  # Начальный размер Кирилла
kira_rect = kira_image.get_rect(center=(screen_width // 2, screen_height // 2))

# Загрузка и увеличение громкости звука скримера
scream_audio = AudioSegment.from_file('./assets/sfx/Scream.mp3')
scream_loud = scream_audio + 6  # Увеличиваем громкость на 200% (6 дБ)
scream_loud.export('./assets/sfx/Scream_loud.mp3', format="mp3")  # Сохраняем увеличенную версию

# Загрузка звуков
laugh_sounds = [
    pygame.mixer.Sound('./assets/sfx/laugh.mp3'),
    pygame.mixer.Sound('./assets/sfx/laugh1.mp3')
]
scream_sound = pygame.mixer.Sound('./assets/sfx/Scream_loud.mp3')  # Загружаем увеличенный звук скримера
sound_index = 0  # Индекс для чередования звуков

# Список смешных фраз с именем Кирилл Тихомиров
funny_phrases = [
    "Кирилл Тихомиров смешно танцует!",
    "Почему ты смотришь на меня, Кирилл?",
    "Хаха, Кирилл Тихомиров ушел влево!",
    "Вот это поворот от Кирилла!",
    "Кирилл, стой!",
    "Кирилл Тихомиров в ударе!",
    "А ну-ка, не двигайся, Кирилл!",
    "Хаха, Кирилл опять здесь!",
    "Кирилл делает супер прыжок!",
    "Быстрее, Кирилл!"
]

# Фон и шрифты
background_color = (255, 228, 225)  # Светлый цвет для фона
spooky_background_color = (0, 0, 0)  # Черный цвет для "жуткого" режима
font = pygame.font.SysFont("Arial", 30, bold=True)
small_font = pygame.font.SysFont("Arial", 20, bold=True)

# Параметры для Кирилла с увеличенной скоростью
kira_speed = [int(5 * 1.5), int(5 * 1.5)]  # Увеличенная скорость
last_phrase_time = pygame.time.get_ticks()
last_event_time = pygame.time.get_ticks()
current_phrase = random.choice(funny_phrases)

# Флаги и таймеры для жуткого эффекта
spooky_mode = False
scream_timer = None
exit_timer = None

def play_laugh_sound():
    global sound_index
    laugh_sounds[sound_index].play()
    sound_index = (sound_index + 1) % len(laugh_sounds)  # Переключение на следующий звук

def stop_all_sounds():
    """Останавливает все звуки, включая фоновую музыку"""
    for sound in laugh_sounds:
        sound.stop()  # Останавливаем каждый звук в массиве

def play_scream():
    """Проигрывает звук скримера на 200% громкости"""
    scream_sound.set_volume(1.0)  # Максимальная громкость для воспроизведения
    scream_sound.play()

def random_event():
    """Функция для генерации случайных событий"""
    global kira_image, kira_rect  # Объявление глобальных переменных в начале функции
    event = random.choice(['resize', 'reverse', 'jump', 'speed_change'])
    if event == 'resize':
        # Увеличение или уменьшение Кирилла
        scale_factor = random.uniform(0.5, 1.5)
        new_size = (int(kira_image.get_width() * scale_factor), int(kira_image.get_height() * scale_factor))
        kira_image = pygame.transform.scale(kira_image, new_size)
        kira_rect = kira_image.get_rect(center=kira_rect.center)
    elif event == 'reverse':
        # Изменение направления
        kira_speed[0] = -kira_speed[0]
        kira_speed[1] = -kira_speed[1]
    elif event == 'jump':
        # Кирилл "прыгает" в случайное место
        kira_rect.x = random.randint(0, screen_width - kira_rect.width)
        kira_rect.y = random.randint(0, screen_height - kira_rect.height)
    elif event == 'speed_change':
        # Изменение скорости
        kira_speed[0] = random.choice([-15, -8, 8, 15])  # Ускоренные значения скорости
        kira_speed[1] = random.choice([-15, -8, 8, 15])

# Основной цикл
running = True
while running:
    # Устанавливаем фон в зависимости от состояния "жуткого" режима
    screen.fill(spooky_background_color if spooky_mode else background_color)

    if spooky_mode:
        # Режим "страшного" эффекта
        stop_all_sounds()  # Отключаем все звуки
        kira_rect.center = (screen_width // 2, screen_height // 2)  # Центрируем Кирилла
        screen.blit(kira_image, kira_rect)  # Отображаем Кирилла в центре
        text = font.render("...", True, (255, 255, 255))
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height - 50))

        # Проверка таймера скримера и таймера выхода
        if scream_timer and time.time() >= scream_timer + 3:
            play_scream()  # Проигрываем скример через 3 секунды
            scream_timer = None  # Сбрасываем таймер для скримера
            exit_timer = time.time()  # Устанавливаем таймер для выхода

        # Закрытие программы через 2 секунды после скримера
        if exit_timer and time.time() >= exit_timer + 2:
            running = False  # Завершаем программу

    else:
        # Нормальный режим
        # Движение Кирилла
        kira_rect = kira_rect.move(kira_speed)
        if kira_rect.left < 0 or kira_rect.right > screen_width:
            kira_speed[0] = -kira_speed[0]
            play_laugh_sound()  # Проигрываем звук, чередуя их
        if kira_rect.top < 0 or kira_rect.bottom > screen_height:
            kira_speed[1] = -kira_speed[1]
            play_laugh_sound()  # Проигрываем звук, чередуя их

        # Случайные фразы каждые 2 секунды
        if pygame.time.get_ticks() - last_phrase_time > 2000:
            current_phrase = random.choice(funny_phrases)
            last_phrase_time = pygame.time.get_ticks()

        # Случайные события каждые 3 секунды
        if pygame.time.get_ticks() - last_event_time > 3000:
            random_event()
            last_event_time = pygame.time.get_ticks()

        # Отображение Кирилла и смешной фразы
        screen.blit(kira_image, kira_rect)
        text = font.render(current_phrase, True, (0, 0, 0))
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height - 50))

        # Отображение надписи вверху
        hint_text = small_font.render("Нажми на пробел чтобы помешать всем веселиться.", True, (0, 0, 0))
        screen.blit(hint_text, (10, 10))

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False  # Нажмите ESC для выхода из полноэкранного режима
            elif event.key == pygame.K_SPACE:
                spooky_mode = True  # Включаем жуткий эффект при нажатии пробела
                scream_timer = time.time()  # Устанавливаем таймер для скримера
                keyboard.block_key("windows")  # Блокируем клавишу Windows

    pygame.display.flip()
    pygame.time.delay(30)  # Небольшая задержка, чтобы не перегружать процессор

# Разблокировка клавиши Windows при выходе
keyboard.unblock_key("windows")
pygame.quit()
sys.exit()
