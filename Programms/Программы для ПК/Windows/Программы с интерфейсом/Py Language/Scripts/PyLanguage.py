from multiprocessing.connection import answer_challenge
import pygame as pg, pyautogui,time,random,math,sys,pickle
pg.font.init()
import sys

sc = pg.display.set_mode((1920, 1080))

pos = pg.mouse.get_pos()

f1 = pg.font.Font(None, 25)

step = 1

radius = 10

draw_dist = 25

horizontal_offset = 10

vertical_offset = 10

questionslist  = ['Who is it?','What is it?']
numbers = ['1','2','3','4','5','6','7','8','9']

questions_max = len(questionslist)
pos = pg.mouse.get_pos()

WHITE = (255, 255, 255)
text1 = f1.render('Вопрос: '+str(numbers[0])+'/'+str(questions_max), True,(180, 0, 0))
f = pg.font.SysFont('serif', 20)
sc.fill(WHITE)
pg.draw.rect(sc, (150, 150,150), (0, 0, 1920, 80))

"""
for i in range( len(Colors)):
    i = pg.draw.circle(sc, Colors[i],(ColorsCoords_x[i],ColorsCoords_y[i]), radius)
"""

sc.blit(text1, (10, 50))
pg.display.update()

def make_screenshot():
    screenshot = pyautogui.screenshot('снимки экрана/screenshot.png',region=(0,80, 1920, 1000))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

        if event.type == pg.KEYDOWN:
            '''
            if event.key == pg.K_s:
                make_screenshot()
            '''
            if event.key == pg.K_q:
                quit()



                
'''         
from typing import List
class Customers:
    def __init__(self,name,age,Product,id):
        self.Name = Name
        self.Age = Age
        self.Product = Product

class Products:
    def __init__(self,name,cost,id):
        self.Name = Name
        self.cost = cost

Name = ['Andrey','Andrey','Andrey','Andrey','Andrey']
Age = ['1','2','3','4','5']
Product = [ ['Product1'],['Product2'],['Product3'],['Product4'],['Product5'] ]

max = len(Age)
for i in range(max):
    print(Name[i],Age[i],Product[i])
    
'''
            
