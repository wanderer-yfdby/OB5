# Выбивалы для LOLшары!
import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Игра на выживание")

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)


# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

        # Ограничение движения игрока рамками экрана
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height


# Класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(-20, 0)
        self.speed_y = random.randint(1, 2)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > screen_height:
            self.rect.x = random.randint(0, screen_width - self.rect.width)
            self.rect.y = random.randint(-20, 0)
            self.speed_y = random.randint(1, 2)


# Основной игровой цикл
def game_loop():
    player_image_path = "gol perekatnaya.png"  # Путь к картинке игрока
    player = Player(player_image_path)
    enemies = pygame.sprite.Group()

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    for _ in range(10):
        enemy = Enemy()
        enemies.add(enemy)
        all_sprites.add(enemy)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()

        # Проверка на столкновение
        if pygame.sprite.spritecollideany(player, enemies):
            print("Тебя выбили, лошара!")
            running = False

        screen.fill(black)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


game_loop()