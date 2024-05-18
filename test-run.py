import pygame
pygame.init()
import time

window_size = (1000,600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Тестовый проект")
# Перенос изображений в программу
image1 = pygame.image.load("thoughtful boy.png")
image_rect1 = image1.get_rect()

image2 = pygame.image.load("gol perekatnaya.png")
image_rect2 = image2.get_rect()

# Скорость перемещения спрайта(объекта).
speed = 5

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Перемещение объкта с помощью мышки
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            image_rect1.x = mouseX - 75
            image_rect1.y = mouseY - 90
    if image_rect1.colliderect(image_rect2):
        print("Думай головой, пацан. А то будешь такой, как я!")
        time.sleep(1)

    # Перемещение объкта кнопками клавиатуры
    # key = pygame.key.get_pressed()
    # if key[pygame.K_LEFT]:
    #     image_rect.x -= speed
    # if key[pygame.K_RIGHT]:
    #     image_rect.x += speed
    # if key[pygame.K_UP]:
    #     image_rect.y -= speed
    # if key[pygame.K_DOWN]:
    #     image_rect.y += speed


    screen.fill((0, 0, 0))
    screen.blit(image1, image_rect1)
    screen.blit(image2, image_rect2)
    pygame.display.flip()

pygame.quit()
