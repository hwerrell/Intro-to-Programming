"""This file handles setting up pygame and executing an animation based on the inputted csv"""

import pygame
import Visual_Objects as vo

#=====
#pygame setup
#=====
HEIGHT = 800 
WIDTH = 1000

pygame.init()

screen = pygame.display.set_mode((WIDTH ,HEIGHT))
pygame.display.set_caption("Spotify Clouds")

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (129,200,230) #Sky background color

clock = pygame.time.Clock()

if __name__ == "__main__":
    # Create the clouds for each song/track
    for i in range(len(vo.year)):
        cloud_instance = vo.Cloud(i)
        vo.clouds.append(cloud_instance)
    
    running = True
    while running:
        screen.fill(BLUE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        #display clouds on the screen
        for cloud in vo.clouds:
            cloud.update(WIDTH)
            cloud.display(screen)
        
        clock.tick(60) #I had some issues with the clouds' speed when moving between computers. I knew was based on the framerate, so I used Claude to help me find documentation for keeping the framerate the same no matter what.
        pygame.display.flip()