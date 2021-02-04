import pygame
import math
def mouse_pressed():
    if pygame.mouse.get_pressed()[0]:
        return True

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
class Line:

    def __init__(self, poz_x_start, poz_y_start, poz_x_last, poz_y_last ):

        self.poz_x_last = poz_x_last
        self.poz_y_last = poz_y_last
        self.poz_x_start = poz_x_start
        self.poz_y_start = poz_y_start
        self.radius = 4
    def draw(self, screen):
        pygame.draw.line(screen, WHITE, [self.poz_x_start, self.poz_y_start] , [self.poz_x_last, self.poz_y_last], self.radius)
        
        #pygame.draw.rect(screen, WHITE, (self.poz_x_start, self.poz_y_start, self.poz_x_last - self.poz_x_start, self.poz_y_last - self.poz_y_start))

class Ball:

    def __init__(self, poz_x, poz_y):
        self.poz_x = poz_x
        self.poz_y = poz_y
        self.image = 0
        self.move_c = 1
        self.timer = 0
        self.move_d = 0
        self.radius = 20
        self.rect = pygame.Rect(self.poz_x - 20, self.poz_y - 20 , 40, 40)
    def draw(self, screen):
        #screen.blit(self.image, (self.poz_x, self.poz_y))
        self.image = pygame.draw.circle(screen, (0, 255, 0), (self.poz_x, self.poz_y), self.radius)
        return self.image
    def movement(self):
        self.poz_y += 3 * self.move_c + self.timer // 5
        self.timer += 1
        if self.timer >= 60:
            self.timer = 60
        self.poz_x += 2 * self.move_d 
        if self.move_c < -1 and self.timer >= -15:
            self.move_d = 0.5
        elif self.move_c < -1 and self.timer == 0:
            self.move_c = 0
        elif self.move_c < -1 and self.timer == 0:
            self.move_c = 1
        
        
    def collider(self, line):
        ball_part_1 = pygame.Rect(self.poz_x - 20, self.poz_y - 20, 40, 40)
        ball_part_2 = pygame.Rect(self.poz_x, self.poz_y - 10, 20, 30)
        line_x = pygame.Rect(line.poz_x_start, line.poz_y_start, line.poz_x_last - line.poz_x_start, line.poz_y_last - line.poz_y_start)
        line_y = pygame.Rect(line.poz_x_start, line.poz_y_start, (line.poz_x_last - line.poz_x_start) , (line.poz_y_last - line.poz_y_start) / 1.5)
        line_f = pygame.Rect(line.poz_x_start + (line.poz_x_last - line.poz_x_start) / 5, line.poz_y_start - (line.poz_y_last - line.poz_y_start) / 5, (line.poz_x_last - line.poz_x_start) / 5, (line.poz_y_last - line.poz_y_start) / 5)
        if (ball_part_1.colliderect(line_x) or ball_part_2.colliderect(line_x)) and line.poz_y_last - line.poz_y_start > -50:
            self.move_c = -1
            self.timer = -30
            print("Colide") 
        elif (ball_part_1.colliderect(line_x) and ball_part_1.colliderect(line_y) or ball_part_1.colliderect(line_f)) and line.poz_y_last - line.poz_y_start < -50 and line.poz_x_last - line.poz_x_start > 0:
            self.move_c = -0.5
            self.timer = -30
            self.move_d = -1
        elif (ball_part_1.colliderect(line_x) and ball_part_1.colliderect(line_y) or ball_part_1.colliderect(line_f)) and line.poz_y_last - line.poz_y_start < -50 and line.poz_x_last - line.poz_x_start < 0:
            self.move_c = -0.5
            self.timer = -30
            self.move_d = 1
    def collider_2(self, line):
        x1 = line.poz_x_start
        y1 = line.poz_y_start
        x2 = self.poz_x
        y2 = self.poz_y
        radius1 = line.radius
        radius2 = self.radius
        distances = []
        collided = False
        for i in range(0, 5):
        
            distance = math.hypot(x1 + 50 * i - x2, y1 - y2) 
            distances.append(distance)

        if distances[0] <= 4 + radius2:
            collided = True
        elif distances[1] <= 4 + radius2:
            collided = True
        elif distances[2] <= 4 + radius2:
            collided = True
        elif distances[3] <= 4 + radius2:
            collided = True
        elif distances[4] <= 4 + radius2:
            collided = True

        if collided == True and line.poz_y_last - line.poz_y_start > -50:
            self.move_c = -1
            self.timer = -30
            print("Colide") 
        if collided == True and line.poz_y_last - line.poz_y_start < -50 and line.poz_x_last - line.poz_x_start > 0:
            self.move_c = -0.5
            self.timer = -30
            self.move_d = -1
        if collided == True and line.poz_y_last - line.poz_y_start < -50 and line.poz_x_last - line.poz_x_start < 0:
            self.move_c = -0.5
            self.timer = -30
            self.move_d = 1
            
    def collider_3(self, line):
        collided = False
        line_rect = pygame.Rect(line.poz_x_start, line.poz_y_start, line.poz_x_last - line.poz_x_start, line.poz_y_last - line.poz_y_start)
        if line_rect.colliderect(self.rect):
            collided = True
            print("Collided")
        if collided and line.poz_y_last - line.poz_y_start > -50:
            self.move_c = -1
            self.timer = -30
            
        elif collided and line.poz_y_last - line.poz_y_start < -50 and line.poz_x_last - line.poz_x_start > 0:
            self.move_c = -0.5
            self.timer = -30
            self.move_d = -1
        elif collided and line.poz_y_last - line.poz_y_start < -50 and line.poz_x_last - line.poz_x_start < 0:
            self.move_c = -0.5
            self.timer = -30
            self.move_d = 1
    def collider4(self, line):
       
        x_collider = False #Creating a bool that keeps track if the x-axis is collided 
        y_collider = False #Creating a bool that keeps track if the y-axis is collided 
        #This list compose the x,y of points in the line that is drawn on the screen
        ch_list = []
        cy_list = []
        #Checking for the x axis if the ball is colliding
        if line.poz_x_start > line.poz_x_last:
            
            checker = line.poz_x_last
            #While loop that makes the points from the start pos to the last pos 
            while checker < line.poz_x_start:
                ch_list.append(checker)
                checker += 2
            for item in ch_list:
                if self.poz_x >= item and self.poz_x <= item + 4: #This piece of code takes the x of the ball and ask if it colliding with one of the points 
                    x_collider = True
                    
        elif line.poz_x_last > line.poz_x_start:
            checker = line.poz_x_start
            while checker < line.poz_x_last:
                ch_list.append(checker)
                checker += 2
            for item in ch_list:
                if self.poz_x >= item and self.poz_x <= item + 4:
                    x_collider = True
                    
        #if self.poz_y < line.poz_y_start and self.poz_y > line.poz_y_last:
            #y_collider = True
        if line.poz_y_start > line.poz_y_last:
            
            checker = line.poz_y_last
            while checker < line.poz_y_start:
                cy_list.append(checker)
                checker += 1
            for item in cy_list:
                if self.poz_y == item: # and self.poz_y <= item + 2:
                    y_collider = True
                    
        if line.poz_y_last > line.poz_y_start:
            checker = line.poz_y_start
            while checker < line.poz_y_last:
                cy_list.append(checker)
                checker += 1
            for item in cy_list:
                if self.poz_y == item: #and self.poz_y <= item + 4:
                    x_collider = True
        
            
        if (x_collider and y_collider) and line.poz_y_last - line.poz_y_start > -50:
           self.move_c = -1
           self.timer = -30
            
        elif (x_collider and y_collider) and line.poz_y_last - line.poz_y_start < -50 and line.poz_x_last - line.poz_x_start > 0:
            self.move_c = -0.5
            self.timer = -30
            self.move_d = -1
        elif (x_collider and y_collider)  and line.poz_y_last - line.poz_y_start < -50 and line.poz_x_last - line.poz_x_start < 0:
            self.move_c = -0.5
            self.timer = -30
            self.move_d = 1
        elif (x_collider and y_collider) and line.poz_y_last - line.poz_y_start > -50 and line.poz_x_last - line.poz_x_start > 0:
            self.move_c = -0.5
            self.timer = -30
            self.move_d = 1
        elif (x_collider and y_collider)  and line.poz_y_last - line.poz_y_start > -50 and line.poz_x_last - line.poz_x_start < 0:
            self.move_c = -0.5
            self.timer = -30
            self.move_d = -1
            
            