
import pygame 
WIDTH = 800
HEIGHT = 600


def main():
    pygame.init()
    

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Horse sound board") #is title
    icon = pygame.image.load("horse.png") #is the picture
    pygame.display.set_icon(icon)

    RUN = True
    while RUN:
        #this is for leaving the program 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                RUN = False

        #this is for keystrokes
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    play(1)
                
                if event.key == pygame.K_2:
                    play(2)

                if event.key == pygame.K_3:
                    play(3)

                if event.key == pygame.K_4:
                    play(4)
                
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_w:
                    RUN = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                x = mouse[0]
                y = mouse[1]
                if (10<=x<=160) and (200<=y<=350):
                    play(1)

                if (180<=x<=330) and (200<=y<=350):
                    play(2)

                if (350<=x<=500) and (200<=y<=350):
                    play(3)

                if (520<=x<=670) and (200<=y<=350):
                    play(4)
        
        screen.fill((255, 255, 153)) #fills the screen

        #adds buttons 
        color_button = (211,211,211)
        color_light=(0,0,0)

        pygame.draw.rect(screen, color_button, [10, 200, 150 , 150])
        pygame.draw.rect(screen, color_button, [180, 200, 150 , 150])
        pygame.draw.rect(screen, color_button, [350, 200, 150 , 150])
        pygame.draw.rect(screen, color_button, [520, 200, 150 , 150])
        
        smallfont = pygame.font.SysFont('Corbel',48) 
        text4 = smallfont.render('Sound 4' , True , color_light)
        text3 = smallfont.render('Sound 3' , True , color_light)
        text2 = smallfont.render('Sound 2' , True , color_light)
        text1 = smallfont.render('Sound 1' , True , color_light)

        screen.blit(text4 , (530 , 250))
        screen.blit(text3 , (360 , 250))
        screen.blit(text2 , (190 , 250))
        screen.blit(text1 , (20 , 250))

        pygame.display.update()

# The functions takes an integer in the list 
# of sounds and then plays it.
# param: num: an int telling us what number we want to make
def play(num):
    pygame.mixer.init()
    if num == 1:
        pygame.mixer.music.load("1.mp3")

    if num == 2:
        pygame.mixer.music.load("2.mp3")
                
    if num == 3:
        pygame.mixer.music.load("3.mp3")
       
    if num == 4:
        pygame.mixer.music.load("4.mp3")
    pygame.mixer.music.play()

       
 
    


    
    


if __name__ == "__main__":
    main()