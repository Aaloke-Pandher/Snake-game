# Snake 
import pygame 
import random  
import math 

pygame.init()
pygame.mixer.init()

# Variables  
GREY = [128, 128, 128] 
WHITE = [255, 255, 255] 
BLUE = [0, 0, 255]  
RED = [255, 0, 0] 
GREEN = [0, 255, 0]  
BLACK = [0, 0, 0]  
TILE_SIZE = 20 
ROWS = 40 
COLUMNS = 30 
SCREEN_WIDTH = TILE_SIZE * ROWS 
SCREEN_HEIGHT = TILE_SIZE * COLUMNS

# Player class 
class Player:
    def __init__(self, x, y, w, h ,c):
        self.parts = [[x, y], [x - TILE_SIZE, y], [x - 2 * TILE_SIZE, y]] 
        self.w = w 
        self.h = h  
        self.c = c  
        self.direction = "right"

    def drawPlayer(self, screen):
        for part in self.parts:
            pygame.draw.rect(screen, self.c, [part[0], part[1], self.w, self.h]) 
    
    def update(self):
        cur_head = self.parts[0]

        if self.direction == "right":
            new_head = [cur_head[0] + TILE_SIZE, cur_head[1]]
            self.parts.insert(0, new_head)
            self.parts.pop()
        elif self.direction == "up":
            new_head = [cur_head[0], cur_head[1] - TILE_SIZE]
            self.parts.insert(0, new_head)
            self.parts.pop() 
        elif self.direction == "down":
            new_head = [cur_head[0], cur_head[1] + TILE_SIZE]
            self.parts.insert(0, new_head)
            self.parts.pop() 
        elif self.direction == "left":
            new_head = [cur_head[0] - TILE_SIZE, cur_head[1]]
            self.parts.insert(0, new_head)
            self.parts.pop()
        


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

class PowerUpCosmetic: 
    def __init__(self, x, y, w, h, c):
        self.x = x 
        self.y = y 
        self.w = w 
        self.h = h   
        self.c = c

    def drawPowerUpCosmetic(self, screen):   
        pygame.draw.ellipse(screen, self.c, [self.x, self.y, self.w, self.h]) 

# Lists 
food = [] 
badFood = [] 
powerUP = [] 
cosmeticPowerUp = [] 
playerList = [] 



# Collision Function 
def rectCollision(rect1, rect2): 
   for part in rect1.parts:
    return part[0] < rect2.x + rect2.w and part[1] < rect2.y + rect2.h and part[0] + rect1.w > rect2.x and part[1] + rect1.h > rect2.y 

# Wall Collision 
def wallCollision(rect, score):  
    for part in rect.parts:
        if part[0] > 800 - rect.w:  
            print("Game Over, you scored: " + str(score) + " points!") 
            pygame.quit()
        elif part[0] < 0: 
            print("Game Over, you scored: " + str(score) + " points!") 
            pygame.quit()
        elif part[1] > 600 - rect.h:
            print("Game Over, you scored: " + str(score) + " points!") 
            pygame.quit()  
        elif part[1] < 0: 
            print("Game Over, you scored: " + str(score) + " points!") 
            pygame.quit() 

player = Player(TILE_SIZE  * 20, TILE_SIZE * 15, TILE_SIZE, TILE_SIZE, GREEN) 
# Main function 
def main():
    pygame.init() 
    # Canvas
    size = (SCREEN_WIDTH, SCREEN_HEIGHT) 
    screen = pygame.display.set_mode(size) 
    frameCount = 1
    Score = 0 
    powerUpCount = 0
    # Sound files
    chompSound = pygame.mixer.Sound("chomp.wav") 
    ouchSound = pygame.mixer.Sound("ough.wav") 
    levelUpSound = pygame.mixer.Sound("levelUp.wav") 
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and player.direction != "down":
                    player.direction = "up"
                if event.key == pygame.K_RIGHT and player.direction != "left":
                    player.direction = "right"
                if event.key == pygame.K_DOWN and player.direction != "up":
                    player.direction = "down"
                if event.key == pygame.K_LEFT and player.direction != "right":
                    player.direction = "left"

        # Draw 
        screen.fill(BLACK)  
        player.drawPlayer(screen)    
        wallCollision(player, Score) 
        # Limit speed
        if frameCount % 15 == 0: 
            player.update()

        # Good Food
        if frameCount % 600 == 0: 
            food.append(Food(random.randrange(0, 750), random.randrange(0, 550), 20, 20, GREEN)) 

        # Bad Food
        if frameCount % 1200 == 0:
            badFood.append(Badfood(random.randrange(0, 750), random.randrange(0, 550), 20, 20, RED)) 

        # Speed Power Up
        if frameCount % 1800 == 0:
            powerUP.append(PowerUp(random.randrange(0, 750), random.randrange(0, 550), 20, 20, BLUE)) 
        
        # Cosmetic Power Up
        if frameCount % 2400 == 0:
            cosmeticPowerUp.append(PowerUpCosmetic(random.randrange(0, 750), random.randrange(0, 550), 20, 20, WHITE)) 

        # Draw good food and bad food collsion 
        for i in range(len(food)): 
            food[i].drawFood(screen) 
        for i in range(len(food)): 
            if rectCollision(player, food[i]): 
                player.parts.append((food[i].x, food[i].y)) 
                pygame.mixer.Sound.play(chompSound)
                food.pop(i) 
                Score += 1
                break 

        # Draw bad food and bad food collsion
        for i in range(len(badFood)):
            badFood[i].drawBadFood(screen)
        for i in range(len(badFood)):
            if rectCollision(player, badFood[i]): 
                player.parts.pop()
                pygame.mixer.Sound.play(ouchSound)
                badFood.pop(i) 
                Score -= 1 
                break 

        # Draw speed power up and power up collsion
        for i in range(len(powerUP)):
            powerUP[i].drawPowerUp(screen) 
        for i in range(len(powerUP)):
            if rectCollision(player, powerUP[i]): 
                powerUpCount += 1
                pygame.mixer.Sound.play(levelUpSound)
                powerUP.pop(i) 
                if frameCount % (15 - powerUpCount * 2) == 0:
                    player.update()
                break 

        # Draw cosmetic power up and power up collsion
        for i in range(len(cosmeticPowerUp)):
            cosmeticPowerUp[i].drawPowerUpCosmetic(screen) 
        for i in range(len(cosmeticPowerUp)):
            if rectCollision(player, cosmeticPowerUp[i]): 
                player.c = [random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)] 
                pygame.mixer.Sound.play(levelUpSound)
                cosmeticPowerUp.pop(i)
                break 

        # Quit if length of snake reaches 0
        if player.w == 0:
            pygame.quit() 
            print("Game Over, you scored: " + str(Score) + " points!")  

        pygame.display.flip() 
 
        # --- Limit frames
        clock.tick(60) 
        frameCount += 1
    # Close window 
    pygame.quit()  
    print("Congratulations you scored: " + str(Score) + " points!")

main()