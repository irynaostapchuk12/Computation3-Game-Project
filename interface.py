import pygame
#from game import game_loop
from utils import *  # no need to import pygame because the import is in utils
from config import *  # importing colors and the like
from utils import under_construction


def interface():

    # initiating pygame
    pygame.init() # calling pygame
    # creating the screen at the set resolution
    screen = pygame.display.set_mode(resolution) # show the user something

    # setting the fonts
    corbelfont = pygame.font.SysFont("Corbel", 50)
    comicsansfont = pygame.font.SysFont("Comic Sans MS", 50)

    # render the text (will be used in the game button)
    game_name_text = corbelfont.render("The Platformer Game", True, white)
    game_name_rect = game_name_text.get_rect(center=(90 + 540 // 2, 180 + 60 // 2))  # text centered in the button

    quit_text = corbelfont.render("QUIT", True, white)
    quit_rect = quit_text.get_rect(center=(250 + 200 // 2, 480 + 60 // 2))  # text centered in the button

    rules_text = corbelfont.render("RULES", True, white)
    rules_rect = rules_text.get_rect(center=(250 + 200 // 2, 320 + 60 // 2))  # text centered in the button

    settings_text = corbelfont.render("SETTINGS", True, white)
    settings_rect = settings_text.get_rect(center=(250 + 200 // 2, 400 + 60 // 2))  # text centered in the button

    credits_text = corbelfont.render("CREDITS", True, white)
    credits_rect = credits_text.get_rect(center=(250 + 200 // 2, 560 + 60 // 2))  # text centered in the button

    store_text = corbelfont.render("STORE", True, white)
    store_rect = store_text.get_rect(center=(250 + 200 // 2, 640 + 60 // 2))

    title_text = comicsansfont.render("Computation III - Project", True, red)
    title_rect = title_text.get_rect(midtop=(360, 10))

    # main interface loop (will run until the user quits)
    while True:

        # getting the mouse position (future need)
        mouse = pygame.mouse.get_pos()

        # event detection (future work)
        for ev in pygame.event.get():
            # seeing if the user hits the red x button
            if ev.type == pygame.QUIT:
                pygame.quit()

            # quit button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if quit_rect.collidepoint(ev.pos):
                    pygame.quit()

            # credits button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if credits_rect.collidepoint(ev.pos):
                    credits_()

            # game_name button
            #if ev.type == pygame.MOUSEBUTTONDOWN:
                #if game_name_rect.collidepoint(ev.pos):
                    #wilderness_explorer()

            # settings button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if settings_rect.collidepoint(ev.pos):
                    under_construction()

            # rules button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if rules_rect.collidepoint(ev.pos):
                    under_construction()

            # store button


        # filling the screen
        screen.fill(deep_black)

        # wilderness explorer button
        pygame.draw.rect(screen, "Black" , [90, 180, 540, 60])
        screen.blit(game_name_text, game_name_rect)

        # rules button
        pygame.draw.rect(screen, grey, [250, 320, 200, 60])
        screen.blit(rules_text, rules_rect)

        # options button
        pygame.draw.rect(screen, grey, [250, 400, 200, 60])
        screen.blit(settings_text, settings_rect)

        # quit button
        pygame.draw.rect(screen, grey, [250, 480, 200, 60])
        screen.blit(quit_text, quit_rect)

        # credits button
        pygame.draw.rect(screen, grey, [250, 560, 200, 60])
        screen.blit(credits_text, credits_rect)

        # store button
        pygame.draw.rect(screen, grey, [250, 640, 200, 60])
        screen.blit(store_text, store_rect)

        # showing the title of the project
        screen.blit(title_text, title_rect)

        # update the display so that the loop changes will appear
        pygame.display.update()

# Under construction screen

def credits_():

    # basic settings #

    screen = pygame.display.set_mode(resolution)

    # creating the fonts:
    corbelfont = pygame.font.SysFont("Corbel", 50)
    comicsansfont = pygame.font.SysFont("Comic Sans MS", 25)

    # creating the rendered texts for the credits
    augusto_text = comicsansfont.render("Augusto Santos, ajrsantos@novaims.unl.pt", True, white)
    diogo_text = comicsansfont.render("Diogo Rastreio, drasteiro@novaims.unl.pt", True, white)
    liah_text = comicsansfont.render("Liah Rosenfeld, lrosenfeld@novaims.unl.pt", True, white)

    augusto_rect = augusto_text.get_rect(midtop = (360, 50))
    diogo_rect = diogo_text.get_rect(midtop = (360, 100))
    liah_rect = liah_text.get_rect(midtop = (360, 150))

    iryna_text = comicsansfont.render("Iryna Ostapchuk (20231629)", True, white)
    rita_text = comicsansfont.render("Rita Graça (2023   )", True, white)
    neves_text = comicsansfont.render("Rodrigo Neves (20231616)", True, white)
    ines_text = comicsansfont.render("Inês Palma", True, white)

    iryna_rect = iryna_text.get_rect(midtop = (360, 200))
    rita_rect = rita_text.get_rect(midtop = (360, 250))
    neves_rect = neves_text.get_rect(midtop = (360, 300))
    ines_rect = ines_text.get_rect(midtop = (360, 350))



    # main loop to detect user input and displaying the credits page
    while True:
        # getting the position of the user's mouse
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():

            # allow the user to quit on (x)
            if ev.type == pygame.QUIT:
                pygame.quit()

            # checking if the user clicked the back button
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 450 <= mouse[0] <= 590 and 600 <= mouse[1] <= 660:
                    interface()

        # displaying my screen
        screen.fill(deep_black)

        # displaying our texts

        screen.blit(augusto_text, augusto_rect)
        screen.blit(diogo_text, diogo_rect)
        screen.blit(liah_text, liah_rect)

        screen.blit(iryna_text, iryna_rect)
        screen.blit(rita_text, rita_rect)
        screen.blit(neves_text, neves_rect)
        screen.blit(ines_text, ines_rect)

        # drawing and displaying the back button
        pygame.draw.rect(screen, dark_red, [450, 600, 140, 60])
        back_text = corbelfont.render("back", True, white)
        back_rect = back_text.get_rect(center=(450 + 140 // 2, 600 + 60 // 2))
        screen.blit(back_text, back_rect)

        # updating the display
        pygame.display.update()

def rules_():
    print("Displaying rules...")


#def wilderness_explorer():
    #game_loop()

