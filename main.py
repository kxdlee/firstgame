import pygame



class Object(pygame.sprite.Sprite):
    def __init__(self, img, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

width = 500
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("krutaya igrulya")

bg = pygame.transform.scale(pygame.image.load("images/bg.png"),(width, height))

run = True

while run:
    window.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False










    pygame.display.update()