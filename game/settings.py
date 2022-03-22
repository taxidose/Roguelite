import random

class Settings:
    # Screen
    SCREEN_WIDTH, SCREEN_HEIGHT = 1024, 768
    MAX_FPS = 60
    HERO_FRAME_COOLDOWN = random.randrange(10, 20)  # Cooldown range for more natural animation

    # Stylesheet
    SS_FRAME_WIDTH, SS_FRAME_HEIGHT = 32, 32
    SS_FRAMES_PER_ROW = 10
    SS_ROWS = 5