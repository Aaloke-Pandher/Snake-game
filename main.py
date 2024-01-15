# Snake 
import pygame 
import random  
import math 

pygame.init()
pygame.mixer.init()

# Colors  
Grey = [128, 128, 128] 
White = [255, 255, 255] 
Blue = [0, 0, 255]  
Red = [255, 0, 0] 
Green = [0, 255, 0]  
Black = [0, 0, 0]  

# Player class 
class Player:
    def __init__(self, x, y, w, h):
        self.x = x 
        self.y = y 
        self.w = w 
        self.h = h 
        self.speed = 2  
        self.xspeed = 2
        self.yspeed = 2
        self.m = 1

    def drawPlayer(self, screen): 
        pygame.draw.rect(screen, Green, [self.x, self.y, self.w, self.h]) 

class Food: 
    def __init__(self, x, y, w, h, c): 
        self.x = x 
        self.y = y 
        self.w = w 
        self.h = h   
        self.c = c

    def drawFood(self, screen):   
        pygame.draw.rect(screen, self.c, [self.x, self.y, self.w, self.h], 2) 

class Badfood: 
    def __init__(self, x, y, w, h, c): 
        self.x = x 
        self.y = y 
        self.w = w 
        self.h = h   
        self.c = c

    def drawBadFood(self, screen):   
        pygame.draw.rect(screen, self.c, [self.x, self.y, self.w, self.h], 2) 

class PowerUp:
    def __init__(self, x, y, w, h, c): 
        self.x = x 
        self.y = y 
        self.w = w 
        self.h = h   
        self.c = c

    def drawPowerUp(self, screen):   
        pygame.draw.ellipse(screen, self.c, [self.x, self.y, self.w, self.h], 2) 

# Find mouse 
def mouse_position():
    pos = pygame.mouse.get_pos() 
    mouse_x = pos[0]
    mouse_y = pos[1]
    return mouse_x, mouse_y   

# Player follow mouse 
def follow_object(ob2, speed):  
    run = (mouse_position()[0] - ob2.x) 
    rise = (mouse_position()[1] - ob2.y) 
    d = math.sqrt(rise**2 + run**2)
    dy = (speed * rise) / d 
    dx = (speed * run) / d 
    ob2.x += dx
    ob2.y += dy
    return dx, dy 

# List of Food 
food = [] 
badFood = [] 
powerUP = []

# Collision Function 
def rectCollision(rect1, rect2): 
   return rect1.x < rect2.x + rect2.w and rect1.y < rect2.y + rect2.h and rect1.x + rect1.w > rect2.x and rect1.y + rect1.h > rect2.y 

# Wall Collision 
def wallCollision(rect, timer, sound, score): 
    if rect.x >= 800 - rect.w:  
        pygame.mixer.Sound.play(sound)
        print("Game Over, you scored: " + str(score) + " points!") 
        if timer % 60 == 0: 
            pygame.quit()
    elif rect.x <= 0: 
        pygame.mixer.Sound.play(sound)
        print("Game Over, you scored: " + str(score) + " points!") 
        if timer % 60 == 0:
            pygame.quit()
    elif rect.y >= 600 - rect.h:
        pygame.mixer.Sound.play(sound)
        print("Game Over, you scored: " + str(score) + " points!") 
        if timer % 60 == 0:
            pygame.quit()  
    elif rect.y <= 0: 
        pygame.mixer.Sound.play(sound)
        print("Game Over, you scored: " + str(score) + " points!") 
        if timer % 60 == 0:
            pygame.quit() 

player = Player(400, 300, 20, 20)
# Main function 
def main():
    pygame.init() 
    # Canvas
    size = (800, 600)
    screen = pygame.display.set_mode(size) 
    frameCount = 1
    Score = 0 
    # Sound files
    chompSound = pygame.mixer.Sound("chomp.wav") 
    ouchSound = pygame.mixer.Sound("ough.wav") 
    levelUpSound = pygame.mixer.Sound("levelUp.wav") 
    crashSound = pygame.mixer.Sound("crash.wav") 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    # Main Program Loop 
    while not done:
        # Main event loop
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True  

        # Draw 
        screen.fill(Black) 
        player.drawPlayer(screen)    
        follow_object(player, player.speed) 
        # Good Food
        if frameCount % 600 == 0: 
            food.append(Food(random.randrange(0, 750), random.randrange(0, 550), 20, 20, Green)) 
        # Bad Food
        if frameCount % 1200 == 0:
            badFood.append(Badfood(random.randrange(0, 750), random.randrange(0, 550), 20, 20, Red)) 
        # Speed Power Up
        if frameCount % 1800 == 0:
            powerUP.append(PowerUp(random.randrange(0, 750), random.randrange(0, 550), 20, 20, Blue)) 
        # Draw good food and bad food collsion 
        for i in range(len(food)): 
            food[i].drawFood(screen) 
        for i in range(len(food)): 
            if rectCollision(food[i], player): 
                player.w = food[i].w + player.w 
                pygame.mixer.Sound.play(chompSound)
                food.pop(i) 
                Score += 1
                break 
        # Draw bad food and bad food collsion
        for i in range(len(badFood)):
            badFood[i].drawBadFood(screen)
        for i in range(len(badFood)):
            if rectCollision(badFood[i], player): 
                player.w = player.w - badFood[i].w 
                pygame.mixer.Sound.play(ouchSound)
                badFood.pop(i) 
                Score -= 1 
                break 
        # Draw speed power up and power up collsion
        for i in range(len(powerUP)):
            powerUP[i].drawPowerUp(screen) 
        for i in range(len(powerUP)):
            if rectCollision(powerUP[i], player): 
                player.speed = player.speed + player.speed * 0.1 
                pygame.mixer.Sound.play(levelUpSound)
                powerUP.pop(i)
                break 
        if player.w == 0:
            pygame.quit() 
            print("Game Over, you scored: " + str(Score) + " points!") 
        # Wall Collision 
        if wallCollision(player, frameCount, crashSound, Score):
            frameCount = 0
            frameCount += 1
        pygame.display.flip()
 
        # --- Limit frames
        clock.tick(60) 
        frameCount += 1
    # Close window 
    pygame.quit()  
    print("Congratulations you scored: " + str(Score) + " points!")

main()