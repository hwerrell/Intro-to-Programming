import csv
import pygame
import random

class CloudStyle:
    def __init__(self, circles):
        self.circles = circles
    
    def draw_outline(self, screen, x, y, d, outline_width=2):
        """Draws black outlines for each cloud""" #These are really just slightly larger black circles behind each cloud.
        for offset_x, offset_y in self.circles:
            pygame.draw.circle(screen, (0, 0, 0), (x + int(offset_x * d), y + int(offset_y * d)), d + outline_width)
    
    def draw(self, screen, x, y, r, g, b, d):
        """Draws a cloud with circles"""
        self.draw_outline(screen, x, y, d)
        for offset_x, offset_y in self.circles:
            pygame.draw.circle(screen, (r, g, b), (x + int(offset_x * d), y + int(offset_y * d)), d) #I used Claude to help with documentation for the circle function (I started with rectangles).

#cloud styles - x/y offset positions for each circle
CloudStyle1 = CloudStyle([(-1, 0), (0, -0.3), (1, 0)])  #3 circles left to right
CloudStyle2 = CloudStyle([(-0.5, 0.5), (0, -.2), (0.5, 0.5)])  #3 circles left to right
CloudStyle3 = CloudStyle([(-1.5, 0), (-0.5, -0.3), (0, 0.2), (0.5, -0.3), (1.5, 0)]) #5 circles left to right

class Cloud:
    def __init__(self, idx):
        self.x = -150 #Moves the clouds left so they start off-screen
        self.y = (-(year[idx]) + 2030) * 11 #Adding the most recent year and multiplying by 11 normalizes clouds on the y axis - I'm sure there's a more mathematical way to do this
        self.width = 20
        self.height = 20
        self.size = pop[idx] / 1.5 #Dividing by 1.5 makes all the clouds a little smaller - just for visual balance
        self.color = energy[idx]
        self.speed = tempo[idx] / 400 #Dividing by 400 slows down all the clouds to about the right speed

        #Randomly assigns one of the three cloud styles
        self.style = random.choice([CloudStyle1, CloudStyle2, CloudStyle3]) #I used Claude to help me with documentation for Python's "random" library

    def display(self, screen):
        """displays clouds on the screen"""
        r = int(self.color * 255)
        g = 255
        b = 255
        self.style.draw(screen, self.x, self.y, r, g, b, int(self.size))

    def update(self, WIDTH):
        """changes position of clouds every frame"""
        self.x = self.x + self.speed
        if self.x >= self.width+200 + WIDTH:
            self.x = -100 #moving it left a bit to reduce pop-in


clouds = []

year = []       #height
pop = []        #size
energy = []     #color
tempo = []      #speed left to right

with open('spotify.csv', newline='', encoding='utf-8') as csvfile: #When moving from Linux to Windows I had an error here, I used Claude to debug and added this utf-8 encoding structure
    file = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(file)
    for row in file:
        year_string = row[4]
        year_string = year_string.split('-') #Removes extraneous data from the CSV to adjust clouds based only on the year
        year.append(int(year_string[0]))
        pop.append(float(row[6]))
        energy.append(float(row[13]))
        tempo.append(float(row[22]))
