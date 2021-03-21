import pygame



class Object(pygame.sprite.Sprite):
    def __init__(self, img, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("krutaya igrulya")

# точка спавна игрока
start_x = 100
start_y = 120

#импорт изображений
bg = pygame.transform.scale(pygame.image.load("images/bg.png"),(width, height))
player_img = pygame.transform.scale(pygame.image.load("images/player.png"),(54, 54))

# создание групп объектов
all_sprites = pygame.sprite.Group()

#создание объектов
player = Object(player_img, start_x, start_y, 1)
all_sprites.add(player)

run = True

while run:
    window.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if event.type == pygame.KEYDOWN:
        if keys[pygame.K_w]:
            player.rect.y -= player.speed
        if keys[pygame.K_s]:
            player.rect.y += player.speed
        if keys[pygame.K_a]:
            player.image = pygame.transform.flip(player_img, True, False)
            player.rect.x -= player.speed
        if keys[pygame.K_d]:
            player.image = player_img
            player.rect.x += player.speed






    all_sprites.draw(window)
    all_sprites.update()
    pygame.display.update()