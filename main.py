from numpy import double
import colors
import pygame
import helpFunc
import screen
import circle

def main():
    """
    The main program creats all the screens for the program:
    creats the buttons, the text boxes for the inputs and the graphics for the ilustraisions
    of the problem with the wanted parameters.
     
    The main program makes sure that all the parameters are "OK" for the program
    and runs the correct functions for the inserted parameters.
    """
    # Set up Pygame
    pygame.init()

    # basic font for user typed
    text_result                 = ''
    base_font                   = pygame.font.Font(None, 24)
    user_text_num_of_warriors   = '5'
    active_num_of_warriors      = False
    user_text_num_of_survivors  = '1'
    active_num_of_survivors     = False
    user_text_num_of_delay      = '1000'
    active_num_of_delay         = False
    user_text_start_from        = '1'
    active_start_from           = False
    user_text_reverse           = 'NO'
    active_reverse              = False
    text                        = base_font.render('start' , True , colors.WHITE, colors.BLACK)

    # Define circle parameters
    points                      = helpFunc.generate_circle_points(circle.num_points, circle.radius, circle.center)
    #print(len(points))
    # print ("yosephus plavious problem:")
    # k = 41
    # helpFunc.yosephus_plavious(k, points)
    
    # create rectangle
    input_num_of_warriors       = pygame.Rect(200, 20, 40, 24)
    input_num_of_survivors      = pygame.Rect(200, 50, 40, 24)
    input_num_of_delay          = pygame.Rect(200, 80, 40, 24)
    input_start_from            = pygame.Rect(200, 110, 40, 24)
    input_revers                = pygame.Rect(200, 140, 40, 24)

    # Pygame loop
    running             = True
    loop                = True
    kill                = False
    show_res            = False
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if screen.start_pos.collidepoint(mouse_pos):
                    if((user_text_num_of_warriors != '') & (user_text_num_of_survivors !='') &
                       (user_text_num_of_delay != '') & (user_text_start_from !='')):
                        points      = helpFunc.generate_circle_points(int(user_text_num_of_warriors), circle.radius, circle.center)
                        show_res    = False
                        loop        = True
                        kill        = True
                else:
                    if input_num_of_warriors.collidepoint(event.pos):
                        user_text_num_of_warriors = ''
                        user_text_num_of_survivors  = '1'
                        active_num_of_warriors  = True
                    else:
                        active_num_of_warriors  = False

                    if input_num_of_survivors.collidepoint(event.pos):
                        user_text_num_of_survivors  = ''
                        active_num_of_survivors     = True
                    else:
                        active_num_of_survivors = False

                    if input_num_of_delay.collidepoint(event.pos):
                        user_text_num_of_delay  = ''
                        active_num_of_delay     = True
                    else:
                        active_num_of_delay  = False

                    if input_start_from.collidepoint(event.pos):
                        user_text_start_from    = ''
                        active_start_from       = True
                    else:
                        active_start_from  = False
                    if (input_revers.collidepoint(event.pos)) & (user_text_reverse == 'NO'):
                        active_reverse       = True
                        user_text_reverse    = 'YES'
                    else:
                        active_reverse       = False
                        user_text_reverse    = 'NO'
                    

            if event.type == pygame.KEYDOWN:
                if active_num_of_warriors == True:
                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:
        
                        # get text input from 0 to -1 i.e. end.
                        user_text_num_of_warriors = user_text_num_of_warriors[:-1]
        
                    # Unicode standard is used for string
                    # formation
                    if helpFunc.check_if_num(int(event.key)):
                        if(int(user_text_num_of_warriors + event.unicode)<100):
                            user_text_num_of_warriors += event.unicode
                            #print(user_text_num_of_warriors)
                if active_num_of_survivors == True:
                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:
        
                        # get text input from 0 to -1 i.e. end.
                        user_text_num_of_survivors = user_text_num_of_survivors[:-1]
        
                    # Unicode standard is used for string
                    # formation
                    if helpFunc.check_if_num(int(event.key)):
                        if(int(user_text_num_of_survivors + event.unicode)< int(user_text_num_of_warriors)):
                            user_text_num_of_survivors += event.unicode
                if active_num_of_delay == True:
                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:
        
                        # get text input from 0 to -1 i.e. end.
                        user_text_num_of_delay = user_text_num_of_delay[:-1]
        
                    # Unicode standard is used for string
                    # formation
                    if (helpFunc.check_if_num_or_dot(int(event.key))):
                        if helpFunc.check_if_num(int(event.key)):
                            if(int(user_text_num_of_delay + event.unicode)<10000):
                                user_text_num_of_delay += event.unicode
                        # if (('.' not in user_text_num_of_delay) & (len(user_text_num_of_delay) != 0)):
                        #     user_text_num_of_delay += event.unicode
                    
                if active_start_from == True:
                    # Check for backspace
                    if event.key == pygame.K_BACKSPACE:
        
                        # get text input from 0 to -1 i.e. end.
                        user_text_start_from = user_text_start_from[:-1]
        
                    # Unicode standard is used for string
                    # formation
                    if helpFunc.check_if_num(int(event.key)):
                        if(int(user_text_start_from + event.unicode) <= int(user_text_num_of_warriors)):
                            user_text_start_from += event.unicode
                        
        # Draw the points
        if (loop == True):
            screen.screen.fill(colors.BLACK)
            loop = False
            for i in range(0,len(points)):
                warrior_img         = pygame.image.load('assets/Worior-removebg-preview.png')  #loads warrior picture
                warrior_img         = pygame.transform.scale(warrior_img,(60,60))                                                                               #Scale the picture to the screen
                screen.screen.blit(warrior_img,(int(points[i][0]),int(points[i][1])))
                text_surface_write  = base_font.render(str(i+1), True, colors.WHITE,colors.BLACK)
                screen.screen.blit(text_surface_write, (int(points[i][0]+25),int(points[i][1]+30)))
                pygame.display.flip() # Update the display
            if kill == True:
                    if (active_reverse == False):
                        text_result = helpFunc.yosephus_plavious(points, int(user_text_num_of_survivors), double(user_text_num_of_delay), int(user_text_start_from)-1)
                    else:
                        text_result = helpFunc.yosephus_plavious_reverse(points, int(user_text_num_of_survivors), double(user_text_num_of_delay), int(user_text_start_from)-1)
                    kill = False
                    text_result = "The Survivals are: "+','.join(str(e) for e in text_result)
                    text_result1 = text_result[0:21]
                    text_result2 = text_result[21:43]
                    text_result = ([(text_result[i:i+22]) for i in range(43, len(text_result), 22)])
                    # text_result = re.sub("(.{20})", "\\1\n", text_result, 0, re.DOTALL) 
                    show_res = True
  
        if active_num_of_warriors:
            color_war = colors.color_active
        else:
            color_war = colors.color_passive
        
        if active_num_of_survivors:
            color_sur = colors.color_active
        else:
            color_sur = colors.color_passive
        if active_num_of_delay:
            color_delay = colors.color_active
        else:
            color_delay = colors.color_passive
        if active_start_from:
            color_start_from = colors.color_active
        else:
            color_start_from = colors.color_passive
        if active_reverse:
            color_reverse = colors.color_active
        else:
            color_reverse = colors.color_passive
            
        # draw rectangle and argument passed which should
        # be on screen
        pygame.draw.rect(screen.screen, color_war, input_num_of_warriors)
        pygame.draw.rect(screen.screen, color_sur, input_num_of_survivors)
        pygame.draw.rect(screen.screen, color_delay, input_num_of_delay)
        pygame.draw.rect(screen.screen, color_start_from, input_start_from)
        pygame.draw.rect(screen.screen, color_reverse, input_revers)
    
        text_surface_war        = base_font.render(user_text_num_of_warriors, True, colors.WHITE)
        text_surface_sur        = base_font.render(user_text_num_of_survivors, True, colors.WHITE)
        text_surface_delay      = base_font.render(user_text_num_of_delay, True, colors.WHITE)
        text_surface_start_from = base_font.render(user_text_start_from, True, colors.WHITE)
        text_surface_reverse    = base_font.render(user_text_reverse, True, colors.WHITE)
        #text_surface_write      = base_font.render("Click for writting", True, colors.WHITE,colors.BLACK)
        text_war                = base_font.render("Number of warriors", True, colors.WHITE,colors.BLACK)
        text_sur                = base_font.render("Number of survivors", True, colors.WHITE,colors.BLACK)
        text_delay              = base_font.render("Delay in seconds", True, colors.WHITE,colors.BLACK)
        text_start_from         = base_font.render("Start from", True, colors.WHITE,colors.BLACK)
        text_reverse            = base_font.render("Reversed", True, colors.WHITE,colors.BLACK)

        if show_res:
            
            text_surface_result1 = base_font.render(text_result1, True, colors.WHITE,colors.BLACK)
            screen.screen.blit(text_surface_result1, (screen.WIDTH//2-50, screen.HEIGHT//4+20))
        
            text_surface_result2 = base_font.render(text_result2, True, colors.WHITE,colors.BLACK)
            screen.screen.blit(text_surface_result2, (screen.WIDTH//2-50, screen.HEIGHT//4 + 40))
            
            if(len(text_result) > 0):
                text_surface_result3 = base_font.render(str(text_result[0]), True, colors.WHITE,colors.BLACK)
                screen.screen.blit(text_surface_result3, (screen.WIDTH//2-50, screen.HEIGHT//4 +60))
            if(len(text_result) > 1):
                text_surface_result4 = base_font.render(str(text_result[1]), True, colors.WHITE,colors.BLACK)
                screen.screen.blit(text_surface_result4, (screen.WIDTH//2-50, screen.HEIGHT//4 +80))
            if(len(text_result) > 2):
                text_surface_result5 = base_font.render(str(text_result[2]), True, colors.WHITE,colors.BLACK)
                screen.screen.blit(text_surface_result5, (screen.WIDTH//2-50, screen.HEIGHT//4 +100))
            if(len(text_result) > 3):
                text_surface_result6 = base_font.render(str(text_result[3]), True, colors.WHITE,colors.BLACK)
                screen.screen.blit(text_surface_result6, (screen.WIDTH//2-50, screen.HEIGHT//4 +120))
            if(len(text_result) > 4):
                text_surface_result7 = base_font.render(str(text_result[4]), True, colors.WHITE,colors.BLACK)
                screen.screen.blit(text_surface_result7, (screen.WIDTH//2-50, screen.HEIGHT//4 +140))
            if(len(text_result) > 5):
                text_surface_result8 = base_font.render(str(text_result[5]), True, colors.WHITE,colors.BLACK)
                screen.screen.blit(text_surface_result8, (screen.WIDTH//2-50, screen.HEIGHT//4 +160))
            if(len(text_result) > 6):
                text_surface_result9 = base_font.render(str(text_result[6]), True, colors.WHITE,colors.BLACK)
                screen.screen.blit(text_surface_result9, (screen.WIDTH//2-50, screen.HEIGHT//4 + 180))
            if(len(text_result) > 7):
                text_surface_result10 = base_font.render(str(text_result[7]), True, colors.WHITE,colors.BLACK)
                screen.screen.blit(text_surface_result10, (screen.WIDTH//2-50, screen.HEIGHT//4 +200))
            if(len(text_result) > 8):
                text_surface_result11 = base_font.render(str(text_result[8]), True, colors.WHITE,colors.BLACK)
                screen.screen.blit(text_surface_result11, (screen.WIDTH//2-50, screen.HEIGHT//4 +220))
            if(len(text_result) > 9):
                text_surface_result12 = base_font.render(str(text_result[9]), True, colors.WHITE,colors.BLACK)
                screen.screen.blit(text_surface_result12, (screen.WIDTH//2-50, screen.HEIGHT//4 +240))
            if(len(text_result) > 10):
                text_surface_result13 = base_font.render(str(text_result[10]), True, colors.WHITE,colors.BLACK)
                screen.screen.blit(text_surface_result13, (screen.WIDTH//2-50, screen.HEIGHT//4 +260))
            if(len(text_result) > 11):
                text_surface_result14 = base_font.render(str(text_result[11]), True, colors.WHITE,colors.BLACK)
                screen.screen.blit(text_surface_result14, (screen.WIDTH//2-50, screen.HEIGHT//4 +280))
            if(len(text_result) > 12):
                text_surface_result15 = base_font.render(str(text_result[12]), True, colors.WHITE,colors.BLACK)
                screen.screen.blit(text_surface_result15, (screen.WIDTH//2-50, screen.HEIGHT//4 +300))
            if(len(text_result) > 13):
                text_surface_result16 = base_font.render(str(text_result[13]), True, colors.WHITE,colors.BLACK)
                screen.screen.blit(text_surface_result16, (screen.WIDTH//2-50, screen.HEIGHT//4 +320))
            if(len(text_result) > 14):
                text_surface_result17 = base_font.render(str(text_result[14]), True, colors.WHITE,colors.BLACK)
                screen.screen.blit(text_surface_result17, (screen.WIDTH//2-50, screen.HEIGHT//4 +340))
        
        # render at position stated in arguments
        screen.screen.blit(text_surface_war, (input_num_of_warriors.x+5, input_num_of_warriors.y+5))
        screen.screen.blit(text_surface_sur, (input_num_of_survivors.x+5, input_num_of_survivors.y+5))
        screen.screen.blit(text_surface_delay, (input_num_of_delay.x+5, input_num_of_delay.y+5))
        screen.screen.blit(text_surface_start_from, (input_start_from.x+5, input_start_from.y+5))
        screen.screen.blit(text_surface_reverse, (input_revers.x+5, input_revers.y+5))
        #screen.screen.blit(text_surface_write, (200, 20))
        screen.screen.blit(text_war, (20, 20))
        screen.screen.blit(text_sur, (20, 50))
        screen.screen.blit(text_delay, (20, 80))
        screen.screen.blit(text_start_from, (20, 110))
        screen.screen.blit(text_reverse, (20, 140))

        # superimposing the text onto our button
        screen.screen.blit(text , screen.start_pos)
        
        # updates the frames of the game
        pygame.display.update()
        
        # set width of textfield so that text cannot get
        # outside of user's text input
        input_num_of_warriors.w     = max(100, text_surface_war.get_width()+10)
        input_num_of_survivors.w    = max(100, text_surface_sur.get_width()+10)
        input_num_of_delay.w        = max(100, text_surface_delay.get_width()+10)
        input_start_from.w          = max(100, text_surface_start_from.get_width()+10)
        input_revers.w              = max(100, text_reverse.get_width()+10)
        
        # screen to updated, not full area
        pygame.display.flip()
        
        # Control the frame rate
        screen.clock.tick(screen.FPS)

    # Quit Pygame properly
    pygame.quit()

main()
