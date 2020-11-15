# coding:utf-8
#view sourcer and anthor:CFT猫鱼树
#You need to install the PYGAME library first！
#look this:
#1,press"windows"and"R"to open runner progrem;
#2,input"cmd"
#3,input"pip install pygame"and wait for few minute
#4,open with"Aptana Studio3"
#thanks for you looking!
from pygame import display,movie
import pygame
from pygame.locals import *
import sys
import random
import time
import os
import easygui as g
import math as m
#set icon
import ctypes
pygame.display.init()
pygame.display.set_icon(pygame.image.load("imgs/logo.png"))
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

#load before game music
if random.randint(1,2) == 1:
    pygame.mixer.init()
    pygame.mixer.music.load("audio/init_bgm_better.mp3")
    pygame.mixer.music.play()
    #tip window
    if g.ccbox("                  game name:tableboom           anthor:cft猫鱼树                  规则:（请滚动阅读）                                                      1，wasd控制，SPACE键停下，敌我方HP各为30，子弹伤害：-2hp，当子弹或血条耗尽则失败2，我方子弹发射的同时，敌方也会发射，请注意搭防                        3，祝你玩得愉快！",image=("imgs/TABLEBOOM.png"),choices=("还不快点开始！","算了吧/(ㄒoㄒ)/~~"),title=("一个小提示")):
        pygame.init()
    else:
        g.msgbox("                                 毕竟难度还是有的嘛~",title=("Goodbye"))
        sys.exit(0)
elif random.randint(1,2) == 2:
    pygame.mixer.init()
    pygame.mixer.music.load("audio/init_bgm.mp3")
    pygame.mixer.music.play()
    #tip window
    if g.ccbox("                  game name:tableboom           anthor:cft猫鱼树                  规则:（请滚动阅读）                                                      1，wasd控制，SPACE键停下，敌我方HP各为30，子弹伤害：-2hp，当子弹或血条耗尽则失败2，我方子弹发射的同时，敌方也会发射，请注意搭防                        3，祝你玩得愉快！",image=("imgs/TABLEBOOM.png"),choices=("走起！","算了吧/(ㄒoㄒ)/~~"),title=("a little tip")):
        pygame.init()
    else:
        g.msgbox("                                      再见~",title=("goodbye"))
        sys.exit(0)
else:
    pygame.mixer.init()
    pygame.mixer.music.load("audio/init_bgm_better.mp3")
    pygame.mixer.music.play()
    #tip window
    if g.ccbox("                  game name:tableboom           anthor:cft猫鱼树                  规则:（请滚动阅读）                                                      1，wasd控制，SPACE键停下，敌我方HP各为30，子弹伤害：-2hp，当子弹或血条耗尽则失败2，我方子弹发射的同时，敌方也会发射，请注意搭防                        3，祝你玩得愉快！",image=("imgs/TABLEBOOM.png"),choices=("走起！","算了吧/(ㄒoㄒ)/~~"),title=("a little tip")):
        pygame.init()
    else:
        g.msgbox("                                      再见~",title=("goodbye"))
        sys.exit(0)
#setting window
os.environ[ 'SDL_VIDEO_WINDOW_POS']="%d,%d"%(130, 65)
canvas = pygame.display.set_mode((972,729))
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
#window's title
pygame.display.set_caption("Table Boom——made_with_CFT")
#mouse postion
def mouse():
    pos = pygame.mouse.get_pos()
    ms_x = pos[0]
    ms_y = pos[1]
#load image and background
my = pygame.image.load("imgs/my.png")
enemy = pygame.image.load("imgs/enemy.png")
BG = pygame.image.load("imgs/BG.png")
tip = pygame.image.load("imgs/background.png")
aim = pygame.image.load("imgs/aim.png")
win = pygame.image.load("imgs/board_win.png")
lose = pygame.image.load("imgs/board_lose.png")
health = pygame.image.load("imgs/mHealth.png")
e_health = pygame.image.load("imgs/eHealth.png")
tititi = pygame.image.load("imgs/TABLEBOOM.png")
b_lable = pygame.image.load("imgs/bulletLable.png")
m_lable = pygame.image.load("imgs/myLable.png")
e_lable = pygame.image.load("imgs/enemyLable.png")
m_bu = pygame.image.load("imgs/m_bullet.png")
e_bu = pygame.image.load("imgs/e_bullet.png")

re = pygame.image.load("imgs/restart.png")
#(debug)load icon
pygame.display.set_icon(pygame.image.load("imgs/logo.png"))

#handle event of function
def handleEvent():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
            pygame.quit()
#muuuuuuuuuusic

def mu():
        pygame.mixer.init()
        pygame.mixer.music.load("audio/bgm.mp3")
        pygame.mixer.music.play(0)
        
#type function
def type(text,position):
    #font is"inkfree"
    TextFont = pygame.font.SysFont('Inkfree',40)
    #setting printting
    newText = TextFont.render(text,True,(0,0,0))   
    canvas.blit(newText,position)
#datas
g_start = 0
g_mode = 1

m_mode = 0

m_x = 50
m_y = 550
e_x = 850
e_y = 100
#game time
t = 180   
#element HP
my_health = 40
enemy_health = 40
#enemy postion by random
r_e_x = 0
r_e_y = 0
r_e_e = 0
#(debug)while point
i = 0
#(debug)event for mouse 
ms_hover_x = 0
ms_hover_y = 0
#bullet data(look down!)

#my
#
#tg
a_t_x = 0
a_t_y = 0
#data of bullet(sporting)
b_s_x = 9999
b_s_y = 9999
#data of hover postion
b_h_x = 0
b_h_y = 0
#data of m_bullet line
b_l = 0
#data of event hover
m_b_h = 0
#data of event hover(my postion)
a_f_x = 9999
a_f_y = 9999
#data of bullet(数量)
b_shuliang = 50





#(degug)time
time = 0
"""


"""
#enemy bullet
#
#data of event hover
e_b_h = 0
#data of enemy bullet's tg
e_t_x = 0
e_t_y = 0
#data of enemy bullet(sporting)
e_b_s_x = 9999
e_b_s_y = 9999
#data of event hover(enemy postion)
e_a_f_x = 9999
e_a_f_y = 9999
#
#
#
#my HP
m_hp_x = 0
m_hp = 30
#enemy HP
e_hp_x = 0
e_hp = 30
###
#win or lose
win_or_lose = 999
#load music(no audio)

#pygame.mixer.music.load("audio/bgm.mp3")
#pygame.mixer.music.play()

#debug(music)
mu()
#debug(....?)
def debug_my_frist():
    canvas.blit(my,(50,550))
def debug_enemy_frist():
    canvas.blit(enemy,(850,100))
    
    
def m_bu_get_out():
    #out
    canvas.blit(m_bu,(9999,9999))
    m_b_h = 0
def e_bu_get_out():
    #out
    canvas.blit(e_bu,(9999,9999))
    e_b_h = 0
#bullet
def m_fire(x,y):
    pass
def e_fire(x,y):
    pass

#Thanks every one
print("祝您玩得愉快！")
print("good luck for you！")
while True:
    if g_mode == 1:
        #print(r_e_e)
        #print(pygame.key.get_pressed())
        m_bu_get_out()
        e_bu_get_out()
        pos = pygame.mouse.get_pos()
        ms_x = pos[0]
        ms_y = pos[1]

        #draw background,and aim
        canvas.blit(BG,(-1,-1))
        canvas.blit(aim,(ms_x-45,ms_y-45))
        #draw tip
        canvas.blit(tip,(100,260))
        canvas.blit(m_lable,(100,500))
        debug_my_frist()
        canvas.blit(e_lable,(850,000))
        debug_enemy_frist()
        if g_start == 1:
            canvas.blit(BG,(-1,-1))
            canvas.blit(my,(m_x,m_y))
            canvas.blit(enemy,(e_x,e_y))
            canvas.blit(aim,(ms_x-45,ms_y-45))
            e_bu_get_out()
            canvas.blit(m_bu,(b_s_x,b_s_y))
            canvas.blit(e_bu,(e_b_s_x,e_b_s_y))
            canvas.blit(health,(m_hp_x,-50))
            canvas.blit(e_health,(e_hp_x,680))
            canvas.blit(b_lable,(50,50))
            
            if b_shuliang == 50:
                type("50",(200,40))
            if b_shuliang == 49:
                type("49",(200,40))
            if b_shuliang == 48:
                type("48",(200,40))
            if b_shuliang == 47:
                type("47",(200,40))
            if b_shuliang == 46:
                type("46",(200,40))
            if b_shuliang == 45:
                type("45",(200,40))
            if b_shuliang == 44:
                type("44",(200,40))
            if b_shuliang == 43:
                type("43",(200,40))
            if b_shuliang == 42:
                type("42",(200,40))
            if b_shuliang == 41:
                type("41",(200,40))
            if b_shuliang == 40:
                type("40",(200,40))
            if b_shuliang == 39:
                type("39",(200,40))
            if b_shuliang == 38:
                type("38",(200,40))
            if b_shuliang == 37:
                type("37",(200,40))
            if b_shuliang == 36:
                type("36",(200,40))
            if b_shuliang == 35:
                type("35",(200,40))
            if b_shuliang == 34:
                type("34",(200,40))
            if b_shuliang == 33:
                type("33",(200,40))
            if b_shuliang == 32:
                type("32",(200,40))
            if b_shuliang == 31:
                type("31",(200,40))
            if b_shuliang == 30:
                type("30",(200,40))
            if b_shuliang == 29:
                type("29",(200,40))
            if b_shuliang == 28:
                type("28",(200,40))
            if b_shuliang == 27:
                type("27",(200,40))
            if b_shuliang == 26:
                type("26",(200,40))
            if b_shuliang == 25:
                type("25",(200,40))
            if b_shuliang == 24:
                type("24",(200,40))
            if b_shuliang == 23:
                type("23",(200,40))
            if b_shuliang == 22:
                type("22",(200,40))
            if b_shuliang == 21:
                type("21",(200,40))
            if b_shuliang == 20:
                type("20",(200,40))
            if b_shuliang == 19:
                type("19",(200,40))
            if b_shuliang == 18:
                type("18",(200,40))
            if b_shuliang == 17:
                type("17",(200,40))
            if b_shuliang == 16:
                type("16",(200,40))
            if b_shuliang == 15:
                type("15",(200,40))
            if b_shuliang == 14:
                type("14",(200,40))
            if b_shuliang == 13:
                type("13",(200,40))
            if b_shuliang == 12:
                type("12",(200,40))
            if b_shuliang == 11:
                type("11",(200,40))
            if b_shuliang == 10:
                type("10",(200,40))
            if b_shuliang == 9:
                type("9",(200,40))
            if b_shuliang == 8:
                type("8",(200,40))
            if b_shuliang == 7:
                type("7",(200,40))
            if b_shuliang == 6:
                type("6",(200,40))
            if b_shuliang == 5:
                type("5",(200,40))
            if b_shuliang == 4:
                type("4",(200,40))
            if b_shuliang == 3:
                type("3",(200,40))
            if b_shuliang == 2:
                type("2",(200,40))
            if b_shuliang == 1:
                type("1",(200,40))
        #my hp
        m_hp_x = m_hp*(972/30)-972
        #enemy hp
        e_hp_x = e_hp*(972/30)-972
        #enemy position
        e_x = e_x+(r_e_x-e_x)/17
        e_y = e_y+(r_e_y-e_y)/17
        #than,there is random data to enemy position
        if t%20 ==0:
            if t%20 ==0 and r_e_e == 1:
                r_e_x = m_x
                r_e_y = m_y
            else:
                r_e_x = random.randint(0,973)
                r_e_y = random.randint(0,729)
        #my bullet
        """
        #debugging for this progrem!!!!!!!!!
        !!!!!!!!!!!!!!
        
        """
        if m_b_h == 1:
            b_s_x = b_s_x+(a_t_x-a_f_x)/20
            b_s_y = b_s_y+(a_t_y-a_f_y)/20
            i = i+1
        if i == 20:
            m_bu_get_out()
            m_b_h == 0
            i = 0
            #(debug log)false
            #<<
        if b_s_x < a_t_x and b_s_y < a_t_y:
            if a_t_x < a_f_x and a_t_y < a_f_y:
                m_bu_get_out()
                m_b_h == 0
                i = 0
            #><
        if b_s_x > a_t_x and b_s_y < a_t_y:
            if a_t_x > a_f_x and a_t_y < a_f_y:
                m_bu_get_out()
                m_b_h == 0
                i = 0
            #<>
        if b_s_x < a_t_x and b_s_y > a_t_y:
            if a_t_x < a_f_x and a_t_y > a_f_y:
                m_bu_get_out()
                m_b_h == 0
                i = 0
            #>>
        if b_s_x > a_t_x and b_s_y > a_t_y:
            if a_t_x > a_f_x and a_t_y > a_f_y:
                m_bu_get_out()
                m_b_h == 0
                i = 0
                
        #if b_s_x
                
        #enemy bullet
        if e_b_h == 1:
            e_b_s_x = e_b_s_x+(e_t_x-e_a_f_x)/10
            e_b_s_y = e_b_s_y+(e_t_y-e_a_f_y)/10
            
            
            
            
            
        #my position like sled,fun!
        if m_mode == "w":
            m_y = m_y-20
        elif m_mode == 0:
            m_x = m_x
            m_y = m_y
            #pass
        if m_mode == "s":
            m_y = m_y+20
        elif m_mode == 0:
            m_x = m_x
            m_y = m_y
            #pass
        if m_mode == "a":
            m_x = m_x-20
        elif m_mode == 0:
            m_x = m_x
            m_y = m_y
            #pass
        if m_mode == "d":
            m_x = m_x+20
        elif m_mode == 0:
            m_x = m_x
            m_y = m_y
            #pass
        #don't out the screen!
        if m_x<0:
            m_x = 973
        if m_x>973:
            m_x = 0
        if m_y<0:
            m_y = 729
        if m_y>729:
            m_y = 0
        #HP setting

        if b_shuliang == 0:
            m_hp = 0
        if b_s_x - e_x < 30 and b_s_y - e_y < 30:
            if b_s_x > e_x and b_s_y > e_y:
                e_hp = e_hp-2

        if e_b_s_x - m_x < 30 and e_b_s_y - m_y < 30:
            if e_b_s_x > m_x and e_b_s_y > m_y:
                m_hp = m_hp-2
        
        if m_hp < 1:
            canvas.blit(BG,(-1,-1))
            canvas.blit(lose,(0,0))
            time = time+1
            win_or_lose = 0
            if time > 60:
                canvas.blit(re,(450,500))
                
        if e_hp < 1:
            canvas.blit(BG,(-1,-1))
            canvas.blit(win,(0,0))  
            time = time+1
            win_or_lose = 1
            if time > 666:
                sys.exit()
        #all event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()
            if g_start == 1:
                if event.type==KEYDOWN:
                     if event.key==K_w:
                         m_mode = "w"
                if event.type==KEYDOWN:
                     if event.key==K_s:
                         m_mode = "s"
                if event.type==KEYDOWN:
                    if event.key==K_d:
                         m_mode = "d"
                if event.type==KEYDOWN:
                    if event.key==K_a:
                         m_mode = "a"
                if event.type==KEYDOWN:
                    if event.key==K_SPACE:
                         m_mode = 0
                if event.type == pygame.MOUSEBUTTONUP:
                    pass
                    pass
                    pass
                    pass
                    pass
                    pass
                    r_e_e = 0
            if event.type==KEYDOWN:
                if event.key==K_RETURN:
                    g_start = 1
                    m_bu_get_out()
                    e_bu_get_out()                
            elif event.type == MOUSEBUTTONDOWN:
                pressed_array = pygame.mouse.get_pressed()
                for index in range(len(pressed_array)):
                    if pressed_array[index]:
                        if index == 0:
                            '''
                            aim_tg_x = 0
                            aim_tg_y = 0
                            '''
                            #print(ms_x,ms_y)
                            b_shuliang = b_shuliang - 1
                            e_b_h = 1
                            e_t_x = m_x + 20
                            e_t_y = m_y + 20
                            
                            r_e_x = random.randint(0,973)
                            r_e_y = random.randint(0,729)
                            pass
                            r_e_x = m_x
                            r_e_y = m_y
                            r_e_e = 1
                            
                            a_t_x = ms_x-10
                            a_t_y = ms_y-10
                            e_a_t_x = m_x + 40
                            e_a_t_y = m_y + 40   
                                                     
                            a_f_x = m_x
                            a_f_y = m_y
                            e_a_f_x = e_x
                            e_a_f_y = e_y
                            
                            b_s_x = a_f_x
                            b_s_y = a_f_y
                            e_b_s_x = e_a_f_x
                            e_b_s_y = e_a_f_y
                            #print('Pressed LEFT Button!')
                            #event for hover
                            m_b_h = 1
                            
                            b_l = m.sqrt((a_t_x-a_f_x)*(a_t_x-a_f_x)+(a_t_y-a_f_y)*(a_t_y-a_f_y))
                            if time > 60:
                                if ms_x - 470 > -20 and ms_x - 470 < 20 :
                                    if ms_y - 523 > -20 and ms_y - 523 < 20 :
                                        sys.exit()
                            if win_or_lose == 1:
                                sys.exit()
                if pygame.mouse.get_pressed() == '(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)':
                    '''
                    aim_tg_x = 0
                    aim_tg_y = 0
                    '''
                    e_b_h = 1
                    r_e_e = 1
                    a_t_x = ms_x-10
                    a_t_y = ms_y-10
                    a_f_x = m_x
                    a_f_y = m_y
                    b_s_x = a_f_x
                    b_s_y = a_f_y
                    #print('Pressed LEFT Button!')
                    #event for hover
                    m_b_h = 1
                    b_l = m.sqrt((a_t_x-a_f_x)*(a_t_x-a_f_x)+(a_t_y-a_f_y)*(a_t_y-a_f_y))
            
        #updata time and mouse postion
        mouse()
        t = t-1
        #updata
        pygame.display.update()
        #event
        handleEvent()
    '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()
            if event.type==KEYDOWN:
                if event.key==K_w:
                    m_y = m_y-30
            if event.type==KEYDOWN:
                if event.key==K_s:
                    m_y = m_y+30
            if event.type==KEYDOWN:
                if event.key==K_d:
                    m_x = m_x+30
            if event.type==KEYDOWN:
                if event.key==K_a:
                    m_x = m_x-30
            if event.type==KEYDOWN:
                if event.key==K_RETURN:
                    g_start = 1
    '''








