import pygame
import line_game_functions as lf
size = [400, 800]
screen = pygame.display.set_mode(size)

BLACK = (0, 0, 0)
WHITE = (255, 255 ,255)

active = True
lines = []
print(lines)
k = 0
line = lf.Line(400, 800, 400, 750)
ball = lf.Ball(200, 0)
lines.append(line)
insert = True
clock = pygame.time.Clock()
while active:
    clock.tick(60)
    k += 1
    if k >= 8:
        k = 0
        insert = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
    screen.fill(BLACK)
    ball.draw(screen)
    ball.movement()
    ball.collider4(lines[0])
    if lines[0].poz_y_last < 400:
        for line in lines:
            line.poz_y_last += 1.0
            line.poz_y_start += 1.0
            
    if ball.poz_y > 800:
        ball.poz_y = 0
    if len(lines) > 1:
        ball.collider4(lines[1])
    #print(k)
    if lf.mouse_pressed() and insert:
        insert = False
        lines.insert(0, lf.Line( lines[0].poz_x_last, lines[0].poz_y_last, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
        print(lines[0].poz_y_last)
        print(lines[0].poz_y_start)
    
    for line in lines:
        line.draw(screen)
    if ball.poz_x < -20 or ball.poz_x > 420:
        active = False
        print("Game Over")
    pygame.display.flip()