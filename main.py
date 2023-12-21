# Snake 
import pygame 
import random  

# Define colors 
Grey = [128, 128, 128] 
White = [255, 255, 255] 
Blue = [0, 0, 255]  
Red = [255, 0, 0] 
Green = [0, 255, 0]  
Black = [0, 0, 0] 
# Global  

# Player class 
class Player:
    def __init__(self, x, y, w, h):
        self.x = x 
        self.y = y 
        self.w = w 
        self.h = h 
        self.xspeed = 5 
        self.yspeed = 5  
    def drawPlayer(self, screen): 
        pygame.draw.rect(screen, Green, [self.x, self.y, self.w, self.h]) 
    def MoveUP(self):
        self.y -= self.yspeed


player = Player(400, 300, 20, 20)
# Main function 
def main():
    pygame.init() 
    # Canvas
    size = (800, 600)
    screen = pygame.display.set_mode(size) 
    frameCount = 1
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
           # Check Key Pressed for Player Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= 5 
        elif keys[pygame.K_RIGHT]:
            player.x += 5 
        elif keys[pygame.K_UP]:
            player.y -= 5     
        elif keys[pygame.K_DOWN]:
            player.y += 5   

        # Draw 
        screen.fill(Black) 
        player.drawPlayer(screen)  
        pygame.display.flip()
 
        # --- Limit frames
        clock.tick(60) 
        frameCount += 1

    # Close window
    pygame.quit()  

main()