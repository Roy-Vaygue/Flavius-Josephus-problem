import math
from time import sleep
import pygame
import screen
from pygame import mixer

mixer.init

dead_img = pygame.image.load('assets/dead-removebg-preview.png')  #loads dead picture
dead_img = pygame.transform.scale(dead_img,(60,60))
def generate_circle_points(x, radius, center):
    """
    Generates a list of (x, y) points that can be used to create a circle
    with `x` number of points, a given `radius`, and a specified `center`.
    :return: list of points for the circle
    :rtype: list
    :param number of points: x number of points
    :param number type: int
    :param radius: size of the circle radius
    :param radius type: int
    :param center: the center point
    :param center type: list
    """
    if(x <= 6):
        radius = 50
    if(x <= 18 and x > 6):                                      #defines the radius size
        radius = 100
    if(x <= 40 and x > 18):
        radius = 250
    angle = math.pi*2 / x
    points = []
    for i in range(x):
        #print (i)
        if((angle * i < 90) & (angle * i >= 0)):                #checks in which quarter of the circle is
            x = int(radius * math.cos(i * angle)) + center[0]
            #print(x)
            y = int(radius * math.sin(i * angle)) + center[1]
            #print(y)
        if((angle * i < 180) & (angle * i >= 90)):              #checks in which quarter of the circle is
            x = int(radius * math.cos(i * angle)) + center[0]
            #print(x)
            y = -int(radius * math.sin(i * angle)) + center[1]
            #print(y)
        if((angle * i < 270) & (angle * i >= 180)):             #checks in which quarter of the circle is
            x = -int(radius * math.cos(i * angle)) + center[0]
            #print(x)
            y = -int(radius * math.sin(i * angle)) + center[1]
            #print(y)
        if((angle * i < 360) & (angle * i >= 270)):             #checks in which quarter of the circle is
            x = -int(radius * math.cos(i * angle)) + center[0]
            #print(x)
            y = int(radius * math.sin(i * angle)) + center[1]
            #print(y)
        points.append((x, y))
    return points

    # print("survive by formula =", \
    #       int(2 * (n - math.pow(\
    #           2, math.floor(math.log(n, 2)))) + 1))
    

def play_sound(rout):
    """
    Gets a rout for a sound file and plays is
    :param rout: the rout of the sound file
    :param rout type: str
    """
    mixer.music.set_volume(0.8) #Set preferred volume
    mixer.music.load(rout)      #Load audio file
    mixer.music.play()          #Play the music

def check_if_num(insert):
    """
    Gets an even key and checks if is a number.
    If is returns True else returns False
    :param event key: the event key
    :param event key type: int
    """
    #print(insert)
    if (insert == 49 or insert == 50 or insert == 51 or 
        insert == 52 or insert == 53 or insert == 54 or 
        insert == 55 or insert == 56 or insert == 57 or 
        insert == 48):
        return True
    else:
        return False
def check_if_num_or_dot(insert):
    """
    Gets an even key and checks if is a number or a .
    If is returns True else returns False
    :param event key: the event key
    :param event key type: int
    """
    #print(insert)
    if (insert == 49 or insert == 50 or insert == 51 or 
        insert == 52 or insert == 53 or insert == 54 or 
        insert == 55 or insert == 56 or insert == 57 or 
        insert == 48 or insert == 46):
        return True
    else:
        return False


def yosephus_plavious(points, survivors, delay, start):
    """
    Gets the list of wanted points, num of wanted survivors and the delay between each kill.
    Returns the list of survivors.
    :param points: a list of the points for the circle
    :param points type: list
    :param survivo: the number of wanted survivors
    :param survivo type: int
    :param delay: the delay in seconds
    :param delay type: double
    :param start: the firs warrior that will kill
    :param start type: int
    :return: returns a list of the survivors
    :rparam: list
    """
    me = start
    i = start + 1
    ok = False
    check = []
    while len(check) != (len(points)-survivors):
        if me > len(points)-1:
            me = 0
        if (me + 1) in check:
            me +=1
        else:
            if (i + 1) in check:
                i +=1
            if i == me:
                i+=1
            if i > len(points) - 1:
                i=0
            if (i+1) not in check:
                screen.screen.blit(dead_img,(int(points[i][0]),int(points[i][1])))
                play_sound('assets/knife-slice-41231.mp3')
                sleep(delay/1000)
                pygame.display.flip() # Update the display
                check.append(i+1)
                #print(me+1," killed ",i+1)
                i += 1
                me+=1
                ok = True
            if ok == True:
                me+=1
                ok = False
            i += 1

    res = [ele for ele in range(len(points)+1) if ele not in check and ele != 0]
    #print (res)
    return res

def yosephus_plavious_reverse(points, survivors, delay, start):
    """
    Gets the list of wanted points, num of wanted survivors and the delay between each kill.
    Returns the list of survivors.
    :param points: a list of the points for the circle
    :param points type: list
    :param survivo: the number of wanted survivors
    :param survivo type: int
    :param delay: the delay in seconds
    :param delay type: double
    :param start: the firs warrior that will kill
    :param start type: int
    :return: returns a list of the survivors
    :rparam: list
    """
    me = start
    i = start - 1
    ok = False
    check = []
    while len(check) != (len(points)-survivors):
        if i == me:
            i-=1
        if i == -1:
            i = len(points)-1
        if i == -2:
            i = len(points)-2
        if (me + 1) in check:
            me -=1
        else:
            if (i + 1) in check:
                i -=1
            if i < 0:
                i = len(points)-1
            if i == me:
                i-=1
            if me == -1:
                me = len(points)-1
            if me == -2:
                me = len(points)-2
            if ((i + 1) not in check) & ((me + 1) not in check) & (me != i):
                screen.screen.blit(dead_img,(int(points[i][0]),int(points[i][1])))
                play_sound('assets/knife-slice-41231.mp3')
                sleep(delay/1000)
                pygame.display.flip() # Update the display
                check.append(i+1)
                #print(me+1," killed ",i+1)
                i -= 1
                me -= 1
                ok = True
            if ok == True:
                me -= 1
                ok = False

    res = [ele for ele in range(len(points)+1) if ele not in check and ele != 0]
    #print (res)
    return res