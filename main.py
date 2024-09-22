import pygame

pygame.init()

win_with = 500
win_heigt = 500

clock = pygame.time.Clock()

window = pygame.display.set_mode((win_with,win_heigt))


font = pygame.font.Font(None, 32)
text = ''
exit = False

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                text = "клавишу y нажали"
            if event.key == pygame.K_q:
                text = "клавишу q нажали"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_y:
                text = "клавишу y отпустили"
            if event.key == pygame.K_q:
                text = "клавишу q отпустили"

    window.fill((0, 255, 0))
    window.blit(font.render(text, True, (255,255,25)),(0,0))
    pygame.display.update() 
    clock.tick(60)