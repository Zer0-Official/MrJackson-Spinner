import pygame

pygame.init()

clock = pygame.time.Clock()
scrn = pygame.display.set_mode((300, 300))
pygame.display.set_caption('Mr. Jackson Spinner')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

mrJ = pygame.transform.scale(pygame.image.load('img/mrj.png'), (300, 300))
img = 1
rotation = 0
rpf = 5
move = False
show = True
x, y = 0, 0
pos = (0, 0)
font = pygame.font.SysFont('arial', 12)

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_q):
            pygame.quit()
        elif e.type == pygame.MOUSEBUTTONDOWN:
            if abs(rpf) > 40:
                rpf = 0
            else:
                if rpf < 0:
                    rpf -= 5
                else:
                    rpf += 5
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                rpf *= -1
            if e.key == pygame.K_f:
                if move:
                    scrn = pygame.display.set_mode((300, 300))
                    move = False
                    x, y = (0, 0)
                else:
                    scrn = pygame.display.set_mode((1280, 690))
                    move = True
            if e.key == pygame.K_j:
                if img == 1:
                    mrJ = pygame.transform.scale(pygame.image.load('img/green.png'), (300, 300))
                    img = 2
                elif img == 2:
                    mrJ = pygame.transform.scale(pygame.image.load('img/coday.png'), (300, 300))
                    img = 3
                elif img == 3:
                    mrJ = pygame.transform.scale(pygame.image.load('img/mrj.png'), (300, 300))
                    img = 1
            if e.key == pygame.K_h:
                if show:
                    show = False
                else:
                    show = True
        elif e.type == pygame.MOUSEMOTION and move:
            pos = e.pos
            x = pos[0] - 150
            y = pos[1] - 150

    scrn.fill(WHITE)
    if show:
        scrn.blit(font.render('Fullscreen/Move: f', True, BLACK), (5, 5))
        scrn.blit(font.render('Direction: space', True, BLACK), (5, 17))
        scrn.blit(font.render('Change Face: j', True, BLACK), (5, 29))
        scrn.blit(font.render('Quit: q', True, BLACK), (5, 41))
        scrn.blit(font.render('Hide: h', True, BLACK), (5, 53))
    rotated = pygame.transform.rotate(mrJ, rotation)
    rotation += rpf
    new_rect = rotated.get_rect(center=mrJ.get_rect(topleft=(x, y)).center)
    scrn.blit(rotated, new_rect)
    pygame.display.update()
    clock.tick(60)
