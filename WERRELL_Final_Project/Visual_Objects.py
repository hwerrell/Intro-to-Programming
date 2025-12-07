import csv
import pygame
import random

class CloudStyle:
    def __init__(self, circles):
        self.circles = circles

    def calc_color(self, color_variation, r, g, b): #Reid helped me with this method and working it into my draw method
        new_r = max(0, r - color_variation)  #Sets a limit so the r value doesn't go below 0
        return (new_r, g, b)
    
    def draw(self, screen, x, y, r, g, b, d):
        """Draws a cloud with circles"""
        for offset_x, offset_y, color_variation in self.circles:
            cloud_color = self.calc_color(color_variation, r, g, b)
            pygame.draw.circle(screen, (cloud_color), (x + int(offset_x * d), y + int(offset_y * d)), d) #I used Claude to help with documentation for the circle function (I started with rectangles).

#cloud styles - x, y, color variation offset for each cloud
CloudStyle1 = CloudStyle([(-1, 0, random.randint(int(.2*255), int(.4*255))), (0, -0.3, random.randint(int(.2*255), int(.4*255))), (1, 0, random.randint(int(.2*255), int(.4*255)))])  #3 circles left to right
CloudStyle2 = CloudStyle([(-0.5, 0.5, random.randint(int(.2*255), int(.4*255))), (0, -.2, random.randint(int(.2*255), int(.4*255))), (0.5, 0.5, random.randint(int(.2*255), int(.4*255)))])  #3 circles left to right
CloudStyle3 = CloudStyle([(-1.5, 0, random.randint(int(.2*255), int(.4*255))), (-0.5, -0.3, random.randint(int(.2*255), int(.4*255))), (0, 0.2, random.randint(int(.2*255), int(.4*255))), (0.5, -0.3, random.randint(int(.2*255), int(.4*255))), (1.5, 0, random.randint(int(.2*255), int(.4*255)))]) #5 circles left to right

#I used Claude and google to help me with python's "random" library and how I could use that to adjust my color variation. I played with these values until I got something that looked good.

class Cloud:
    def __init__(self, idx):
        self.x = -150 #Moves the clouds left so they start off-screen
        self.y = (-(year[idx]) + 2030) * 11 #Adding the most recent year and multiplying by 11 normalizes clouds on the y axis - I'm sure there's a more mathematical way to do this
        self.width = 20
        self.height = 20
        self.size = pop[idx] / 1.5 #Dividing by 1.5 makes all the clouds a little smaller - just for visual balance
        self.color = energy[idx] * 1.25 #Multiplying by 1.25 makes all the clouds a little lighter and normalizes the color variations
        self.speed = tempo[idx] / 400 #Dividing by 400 slows down all the clouds to about the right speed

        #Randomly assigns one of the three cloud styles
        self.style = random.choice([CloudStyle1, CloudStyle2, CloudStyle3])

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

with open('spotify.csv', newline='', encoding='utf-8') as csvfile:
    file = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(file)
    for row in file:
        year_string = row[4]
        year_string = year_string.split('-') #Removes extraneous data from the CSV to adjust clouds based only on the year
        year.append(int(year_string[0]))
        pop.append(float(row[6]))
        energy.append(float(row[13]))
        tempo.append(float(row[22]))